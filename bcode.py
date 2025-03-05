import streamlit as st
import cv2
import mysql.connector
from PIL import Image
from pyzbar.pyzbar import decode
from datetime import date
import os
import numpy as np

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ai_chotu"
)
mycursor = mydb.cursor()
current_date = date.today()

def scan_barcode():
    # Capture video
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if not ret:
        st.error("Error: Could not access the camera!")
        cap.release()
        return

    # Save and display image
    image_path = "captured_image.png"
    cv2.imwrite(image_path, frame)
    cap.release()

    if not os.path.exists(image_path):
        st.error("Error: Image not saved properly!")
        return

    # Display captured image
    st.image(Image.open(image_path))
    st.success("Image captured successfully!")

    # Convert to grayscale and decode
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray_image)

    if not decoded_objects:
        st.warning("No barcode detected! Try adjusting the angle or lighting.")
        return

    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        st.write("Data:", data)

        try:
            product_no = int(data)
            mycursor.execute("SELECT * FROM product_detail WHERE Product_No = %s", (product_no,))
            result = mycursor.fetchone()

            if result:
                st.success("Product Found!")
                st.write(f"Product No: {result[1]}")
                st.write(f"Product Name: {result[2]}")
                st.write(f"MFD: {result[3]}")
                st.write(f"EFD: {result[4]}")
                st.write(f"Quantity: {result[5]}")
                st.write(f"Price: {result[6]}")
                st.write(f"Lot Price: {result[7]}")
                st.write(f"Category: {result[8]}")

                if current_date >= result[4]:
                    st.warning("The product is expired")
                else:
                    st.success("The product is not expired")

                # Update product quantity
                mycursor.execute("UPDATE product_detail SET Quantity = Quantity - 1 WHERE Product_No = %s", (product_no,))
                mydb.commit()
                st.success("Product Sales Updated!")
            else:
                st.warning("Product Not Found!")
        except ValueError:
            st.error("Error: Invalid barcode format!")

def bcod():
    st.title("Barcode Scanner")
    if st.button("Scan Barcode"):
        scan_barcode()

    if st.button("Close Database Connection"):
        mycursor.close()
        mydb.close()
        st.success("Database connection closed.")

if __name__ == "__main__":
    bcod()
