import mysql.connector
import json
import requests
from datetime import date, datetime, timedelta
from decimal import Decimal
from groq import Groq
import pandas as pd

# Function to convert date and Decimal objects to string
def serialize_dates(obj):
    if isinstance(obj, date):
        return obj.isoformat()  # Convert date to ISO format string
    elif isinstance(obj, Decimal):
        return float(obj)  # Convert Decimal to float
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ai chotu"
    )

def fetch_and_query_product_data(user_query):
    try:
        # Check if it's an expiry-related query
        if any(word in user_query.lower() for word in ['expir', 'expiring', 'expire']):
            return get_expiring_products()
            
        # Database configuration
        db_config = {
            'host': 'localhost',  # or '127.0.0.1'
            'user': 'root',       # default username for XAMPP
            'password': '',       # default password for XAMPP
            'database': 'ai chotu'  # your database name
        }

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Fetch product details
        cursor.execute("SELECT * FROM product_detail")
        product_data = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()

        # Prepare data for Groq AI
        formatted_data = json.dumps(product_data, default=serialize_dates)

        # Groq AI integration
        client = Groq(api_key="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")

        # Prepare the payload for the API request
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"Here is the product data from the database: {formatted_data}. Please answer questions based on this data."
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Collect the response
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response
        
    except mysql.connector.Error as err:
        return f"Database error: {err}"
    except Exception as e:
        return f"An error occurred: {e}"

def get_expiring_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get current date
        current_date = datetime(2025, 2, 27)  # Using the provided current date
        
        # Define date ranges for different warning levels
        critical_date = current_date + timedelta(days=7)  # Products expiring within 7 days
        warning_date = current_date + timedelta(days=30)  # Products expiring within 30 days
        
        # Query to get expiring products with their details
        query = """
        SELECT 
            p.Product_No,
            p.Product_Name,
            p.Price,
            p.Quantity,
            p.Expiry_Date,
            DATEDIFF(p.Expiry_Date, %s) as days_until_expiry
        FROM 
            product_detail p
        WHERE 
            p.Expiry_Date <= %s
        ORDER BY 
            p.Expiry_Date ASC
        """
        
        cursor.execute(query, (current_date, warning_date))
        products = cursor.fetchall()
        
        if not products:
            return "No products are expiring within the next 30 days."
        
        # Format the response
        response = " Expiring Products Alert:\n\n"
        
        # Categorize products by expiry urgency
        critical_products = []
        warning_products = []
        
        for product in products:
            product_no, name, price, quantity, expiry_date, days_until_expiry = product
            
            product_info = f"• {name} (ID: {product_no})\n"
            product_info += f"  - Price: ₹{price:.2f}\n"
            product_info += f"  - Quantity: {quantity}\n"
            product_info += f"  - Expires: {expiry_date.strftime('%Y-%m-%d')}\n"
            product_info += f"  - Days until expiry: {days_until_expiry}\n"
            
            if expiry_date <= critical_date:
                critical_products.append(product_info)
            else:
                warning_products.append(product_info)
        
        if critical_products:
            response += " Critical (Expiring within 7 days):\n"
            response += "\n".join(critical_products)
            response += "\n"
        
        if warning_products:
            response += "\n Warning (Expiring within 30 days):\n"
            response += "\n".join(warning_products)
        
        cursor.close()
        conn.close()
        
        return response
        
    except mysql.connector.Error as err:
        return f"Database error: {err}"
    except Exception as e:
        return f"An error occurred: {e}"
