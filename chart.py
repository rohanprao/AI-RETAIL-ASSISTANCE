import streamlit as st
import mysql.connector
import pandas as pd

# Ensure page config is the FIRST Streamlit command
st.set_page_config(page_title="AI Chotu Sales Dashboard", layout="wide")

def fetch_sales_data():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'ai_chotu'
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Check if tables exist
        cursor.execute("SHOW TABLES LIKE 'product_detail'")
        if not cursor.fetchone():
            st.error("⚠️ Table 'product_detail' does not exist in the database.")
            return pd.DataFrame(), pd.DataFrame()

        cursor.execute("SHOW TABLES LIKE 'saletrack'")
        if not cursor.fetchone():
            st.error("⚠️ Table 'saletrack' does not exist in the database.")
            return pd.DataFrame(), pd.DataFrame()

        # Fetch Data
        cursor.execute("SELECT * FROM product_detail")
        product_data = cursor.fetchall()

        cursor.execute("SELECT * FROM saletrack")
        sales_data = cursor.fetchall()

        cursor.close()
        conn.close()

        return pd.DataFrame(product_data), pd.DataFrame(sales_data)

    except mysql.connector.Error as err:
        st.error(f"❌ Database Error: {err}")
        return pd.DataFrame(), pd.DataFrame()

# Run the dashboard
def main():
    st.title("📊 AI Chotu Sales Dashboard")

    product_df, sales_df = fetch_sales_data()
    
    if product_df.empty or sales_df.empty:
        return  # Stop execution if data is missing

    st.subheader("Product Data")
    st.write(product_df)

if __name__ == "__main__":
    main()
