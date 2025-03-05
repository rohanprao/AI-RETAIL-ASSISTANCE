import streamlit as st
from groq import Groq
from dbtalk import fetch_and_query_product_data
from sqlquery import execute_sql_query
import speech_recognition as sr
from bcode import bcod
from chart import main as analytics_dashboard
import os

# Custom CSS for the sidebar and main content
st.markdown("""
<style>
    /* Sidebar styling */
    section[data-testid="stSidebar"] > div {
        background-color: #1e293b;
    }
    
    /* Sidebar text color */
    section[data-testid="stSidebar"] .css-1aumxhk, 
    section[data-testid="stSidebar"] .css-zt5igj,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    
    /* Main content styling */
    .main .block-container {
        padding-top: 2rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
    
    /* Card styling */
    .card {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .card h3 {
        color: #1e40af;
        margin-top: 0;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

# Function to convert text to speech and play it
def text_to_speech(text):
    # Function disabled - no sound output
    pass

# Function to capture voice input
def capture_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try: 
        st.write("Recognizing...")
        user_input = r.recognize_google(audio, language='en-in')
        st.write(f"You said: {user_input}")
        return user_input
    except Exception as e:
        st.write("Sorry, I could not understand the audio.")
        return None

# Function to handle user input
def handle_user_input(user_input, from_voice=False):
    # Initialize Groq client
    client = Groq(api_key="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")

    # Classify user intent
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{
            "role": "system",
            "content": "Classify the following user input into 'action' (for database actions like insert, add, delete) or 'inquiry' (for questions about the database). Give one-word reply."
        }, {
            "role": "user",
            "content": user_input
        }],
        temperature=0,
        max_tokens=10,
        top_p=1,
        stream=False,
        stop=None,
    )

    # Get the classification result
    intent = completion.choices[0].message.content.strip().lower()
    
    if intent == 'inquiry':
        # For inquiries, connect to the database and execute the query
        result = fetch_and_query_product_data(user_input)
        return result
    elif intent == 'action':
        # For actions, use SQL execution function
        result = execute_sql_query(user_input)
        return result
    else:
        return "Unable to determine the intent. Please clarify your request."

# Function to create the Streamlit interface
def create_streamlit_interface():
    # User input options in a nice card
    st.markdown("""
    <div class="card">
    <h3>💬 Query Input Options</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for different input methods
    tab1, tab2, tab3, tab4 = st.tabs(["✏️ Text Input", "🎤 Voice Input", "📊 Analytics", "❓ Help & Examples"])
    
    with tab1:
        col1, col2 = st.columns([3, 1])
        with col1:
            user_input = st.text_input("", placeholder="Enter your database query here...", key="text_query")
        with col2:
            submit_button = st.button("🔍 Execute", key="submit_text", use_container_width=True)
        
        if submit_button:
            if user_input:
                with st.spinner("Processing your query..."):
                    output = handle_user_input(user_input)
                    if output:  # Only speak for non-SQL responses
                        st.markdown("""
                        <div class="card">
                        <h3>🤖 AI Response</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        st.success(output)
                        # text_to_speech(output)  # Voice output disabled
                    else:
                        st.info("✅ SQL operation executed without vocal feedback.")
            else:
                st.warning("⚠️ Please enter a query.")
    
    with tab2:
        col1, _ = st.columns([1, 3])
        with col1:
            voice_button = st.button("🎤 Start Listening", key="voice_button", use_container_width=True)
        
        if voice_button:
            with st.spinner("Listening..."):
                user_input = capture_voice_input()
                if user_input:
                    with st.spinner("Processing your query..."):
                        output = handle_user_input(user_input, from_voice=True)
                        if output:  # Only speak for non-SQL responses
                            st.markdown("""
                            <div class="card">
                            <h3>🤖 AI Response</h3>
                            </div>
                            """, unsafe_allow_html=True)
                            st.success(output)
                            # text_to_speech(output)  # Voice output disabled
                        else:
                            st.info("✅ SQL operation executed without vocal feedback.")
    
    with tab3:
        analytics_dashboard()  # Remove the initialize_page parameter since it's now optional

    with tab4:
        st.markdown("""
        <div class="card">
            <h3>🔍 Example Queries</h3>
            <p>Here are some example queries you can try:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Inquiry Examples
        st.markdown("#### 📝 Inquiry Examples")
        st.info("""
        - "Show me all products in stock"
        - "What are the top selling products?"
        - "Show sales for last month"
        - "What is the price of product number 101?"
        - "List all products in the Electronics category"
        """)
        
        # Action Examples
        st.markdown("#### ⚡ Action Examples")
        st.info("""
        - "Add new product: Laptop with price 999.99 in Electronics category"
        - "Update price of product 101 to 45.99"
        - "Delete product number 105"
        - "Record sale of 5 units of product 101"
        """)
        
        # Usage Tips
        st.markdown("""
        <div class="card">
            <h3>💡 Usage Tips</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("""
        1. **Text Input**: Type your query in natural language
        2. **Voice Input**: Click the microphone button and speak your query
        3. **Analytics**: View detailed sales and product analytics
        4. **Be Specific**: Include relevant details like product numbers, prices, or dates
        5. **Natural Language**: You can ask questions in plain English
        """)
        
        # Additional Help
        st.markdown("""
        <div class="card">
            <h3>🎯 Query Guidelines</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("""
        - For inquiries about products or sales, use question words (what, how, when, etc.)
        - For actions (add, update, delete), clearly state the action and provide necessary details
        - Use product numbers when available for more accurate results
        - Specify date ranges for sales-related queries
        - Include category names when searching for specific product types
        """)

# Run the Streamlit interface
if __name__ == "__main__":
    create_streamlit_interface()
