import streamlit as st
import base64
from PIL import Image
import os
import requests
from io import BytesIO

# Force Streamlit to use port 8504
os.environ['STREAMLIT_SERVER_PORT'] = '8504'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_SERVER_ENABLECORS'] = 'false'

# Set page config - MUST be the first Streamlit command
st.set_page_config(
    page_title="AI Chotu",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import other modules after set_page_config
from main import create_streamlit_interface
from chart import main
from bcode import bcod

# Function to download image if it doesn't exist
def download_background_image():
    image_path = "formal_background.jpg"
    if not os.path.exists(image_path):
        # Professional abstract background image URL with blue tones
        image_url = "https://img.freepik.com/free-vector/blue-white-gradient-abstract-background_53876-120239.jpg"
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save(image_path)
    return image_path

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    # Create CSS with background image and lighter overlay for better readability
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.85);  /* 85% white overlay for better contrast */
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Download and set background image
background_image_path = download_background_image()
add_bg_from_local(background_image_path)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #1e40af; margin-bottom: 5px;">AI Chotu</h2>
        <p style="font-size: 14px; color: #475569;">Intelligent Database Assistant</p>
        <hr style="margin: 10px 0; border-color: #e2e8f0;">
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("<p style='font-weight: 500; color: #475569; font-size: 14px; margin-bottom: 10px;'>NAVIGATION</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "",
        ["🏠 Main Page", "📊 Analytics Dashboard", "📷 Barcode Scanner"],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr style='margin: 20px 0; border-color: #e2e8f0;'>", unsafe_allow_html=True)
    
    # About section
    st.markdown("""
    <div style="background-color: rgba(37, 99, 235, 0.05); padding: 15px; border-radius: 8px; margin-top: 20px;">
        <h4 style="color: #1e40af; margin-top: 0; font-size: 16px;">About AI Chotu</h4>
        <p style="font-size: 14px; color: #475569; margin-bottom: 0;">
            AI Chotu is an intelligent assistant that helps you interact with your product database using natural language.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main content area with custom styling for each page
st.markdown('<div class="animated">', unsafe_allow_html=True)

# Load the selected page
if page == "🏠 Main Page":
    st.markdown('<div class="main-page animated">', unsafe_allow_html=True)
    st.markdown('<h1 class="nav-title">AI Retail Assistant</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 18px; line-height: 1.6;">
    Welcome to AI Chotu! Your intelligent assistant for managing product databases through natural language processing.
    </p>
    """, unsafe_allow_html=True)
    
    # Info box
    st.info("""
    ### 🚀 Getting Started
    
    Simply type your query in natural language or use voice commands to interact with your product database.
    Try asking questions like "Show me all products" or "Update the price of product X to Y".
    """)
    
    # Main page layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>💬 Natural Language</h3>
            <p>Interact with your database using everyday language. No need to learn complex query syntax.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>📊 Data Analytics</h3>
            <p>Visualize sales trends and get insights from your product data with interactive charts.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>📱 Multi-Modal</h3>
            <p>Use text, voice, or barcode scanning to interact with your database in different ways.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Load the main interface
    create_streamlit_interface()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 Analytics Dashboard":
    st.markdown('<div class="chart-page">', unsafe_allow_html=True)
    st.title("📊 Sales Analytics Dashboard")
    st.markdown("""
    <p style="font-size: 18px; line-height: 1.6;">
    Analyze your sales data, identify trends, and get predictions for future sales.
    </p>
    """, unsafe_allow_html=True)
    
    from chart import main
    main()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📷 Barcode Scanner":
    st.markdown('<div class="bcode-page">', unsafe_allow_html=True)
    st.title("📷 Barcode Scanner")
    st.markdown("""
    <p style="font-size: 18px; line-height: 1.6;">
    Scan product barcodes to quickly retrieve product information and update inventory.
    </p>
    """, unsafe_allow_html=True)
    
    from bcode import bcod
    bcod()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p>&copy; 2025 Database Management System | All Rights Reserved</p>
        <p style="font-size: 12px; margin-top: 5px;">Version 1.0.0 | Enterprise Edition</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)