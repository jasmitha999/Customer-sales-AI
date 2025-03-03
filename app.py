import streamlit as st
import pandas as pd
import time
from main import (
    initialize_google_sheets,
    record_audio_chunk,
    transcribe_audio,
    analyze_sentiment,
    extract_laptop_name,
    get_deal_recommendations,
    negotiation_coach,
    get_previous_interaction,
    summarize_conversation,
    find_customer_row,
    append_to_existing_customer_row,
    append_new_customer_row,
)

# Load laptop dataset
laptop_data = pd.read_csv("laptop_dataset_updated.csv")  # Path to the dataset
laptop_data = laptop_data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# Streamlit UI Configuration
st.set_page_config(page_title="Laptop Recommendation Assistant", page_icon="💻", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #0073e6;
        text-align: center;
    }
    .section-header {
        font-size: 24px;
        font-weight: bold;
        color: #444;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .box {
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        background-color: #f5f5f5;
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    .red-box {
        background-color: #f44336;
        color: white;
    }
    .green-box {
        background-color: #4caf50;
        color: white;
    }
    .dark-blue-box {
        background-color: #1e3d58;
        color: white;
    }
    .violet-box {
        background-color: #8A2BE2;
        color: white;
    }
    .sky-blue-box {
        background-color: #87ceeb;
        color: white;
    }
    .yellow-box {
        background-color: #ffeb3b;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True
)

# Page Title
st.markdown('<div class="title">AI-Powered Laptop Recommendation and Negotiation Assistant</div>', unsafe_allow_html=True)

# Google Sheets Setup
credentials_path = "credentials.json"
spreadsheet_id = "1BQRX513_GAiLKokObbJoA30foTKzLC_BFS48LD5MMTM"
# Initialize Google Sheets
sheet = initialize_google_sheets(credentials_path, spreadsheet_id)

# Fetch customer history from Google Sheets
def load_customer_history(sheet):
    try:
        data = sheet.get_all_records()
        return pd.DataFrame(data)  # Convert to Pandas DataFrame
    except Exception as e:
        print(f"Error loading customer history: {e}")
        return pd.DataFrame()  

customer_history = load_customer_history(sheet)

# Customer input
customer_name = st.text_input("Enter Customer Name:", key="customer_name")

# Customer Interaction Section
st.markdown('<div class="section-header">Customer Interaction</div>', unsafe_allow_html=True)

# Check for previous interactions
if customer_name:
    previous_summary, deal_status = get_previous_interaction(customer_name, customer_history)
    if previous_summary:
        st.markdown(f'<div class="box violet-box">📌 <strong>Previous Interaction:</strong> {previous_summary}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box violet-box">✅ <strong>Deal Status:</strong> {deal_status}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="box sky-blue-box">🔍 No previous conversation found for this customer.</div>', unsafe_allow_html=True)

# Initialize session state variables
if "recording" not in st.session_state:
    st.session_state.recording = False
    st.session_state.text_input_active = False
    st.session_state.conversation = []  # Store conversation history

# Function to start recording
def start_recording():
    """Start recording and process audio"""
    st.session_state.recording = True

# Buttons for customer input method selection
st.markdown("### Choose Input Method:")
record_button = st.button("🎙️ Record Customer Audio", on_click=start_recording)
text_input_button = st.button("📝 Enter Customer Text Input")

# If text input button is clicked, activate text input
if text_input_button:
    st.session_state.text_input_active = True

# Display text input box only if button was clicked
if st.session_state.text_input_active:
    customer_text_input = st.text_area("Enter Customer Input:", key="customer_text")

    if customer_text_input:
        text = customer_text_input.strip()
        st.session_state.conversation.append(text)
        st.markdown(f'<div class="box dark-blue-box">💬 <strong>Customer Input:</strong> {text}</div>', unsafe_allow_html=True)

# Processing recording
if st.session_state.recording:
    st.markdown('<div class="box dark-blue-box">🎙️ Recording customer input for 6 seconds...</div>', unsafe_allow_html=True)
    audio_file = record_audio_chunk(duration=6)
    text = transcribe_audio(audio_file)

    if text:
        st.session_state.conversation.append(text)
        st.markdown(f'<div class="box dark-blue-box">💬 <strong>Customer Input:</strong> {text}</div>', unsafe_allow_html=True)

# Process conversation after input
if st.session_state.conversation:
    # **End conversation if "end" is detected**
    if "end" in st.session_state.conversation[-1].lower():
        # Remove "end" from the conversation
        filtered_conversation = [t for t in st.session_state.conversation if "end" not in t.lower()]
        if filtered_conversation:
            # Get sentiment of the last meaningful line before "end"
            last_meaningful_line = filtered_conversation[-1]
            final_sentiment = analyze_sentiment(last_meaningful_line)
        else:
            final_sentiment= analyze_sentiment(st.session_state.conversation[-1])  # Default to last detected sentiment
        # Determine deal status based on final sentiment
        final_deal_status = "closed" if final_sentiment == "Positive" else "not closed"
        # Generate summary of the conversation
        summary = summarize_conversation(filtered_conversation)
        # Store in Google Sheets
        row_index = find_customer_row(sheet, customer_name)
        if row_index:
            append_to_existing_customer_row(sheet, row_index, filtered_conversation, summary, final_sentiment, final_deal_status)
        else:
            append_new_customer_row(sheet, customer_name, filtered_conversation, summary, final_sentiment, final_deal_status)
        # Clear the UI and display only final results
        st.session_state.conversation = []  # Clear conversation history

        st.markdown(f'<div class="box violet-box">✅ <strong>Final Summary:</strong> {summary}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box violet-box">📌 <strong>Deal Status:</strong> {final_deal_status}</div>', unsafe_allow_html=True)
        st.markdown('<div class="box green-box">✅ Customer Interaction logged successfully!</div>', unsafe_allow_html=True)

    # Stop further execution
        st.stop()

    sentiment = analyze_sentiment(st.session_state.conversation[-1])
    sentiment_color = "green-box" if sentiment == "Positive" else "red-box" if sentiment == "Negative" else "yellow-box"
    st.markdown(f'<div class="box {sentiment_color}">📊 <strong>Sentiment:</strong> {sentiment}</div>', unsafe_allow_html=True)

    # Extract laptop name
    laptop_name, laptop_row = extract_laptop_name(st.session_state.conversation[-1], laptop_data)
    if laptop_name:
        st.markdown(f'<div class="box violet-box">💻 <strong>Matched Laptop:</strong> {laptop_name}</div>', unsafe_allow_html=True)

    # Get deal recommendations
    answer, recommendations, focused_laptops = get_deal_recommendations(st.session_state.conversation[-1], customer_name, laptop_data, [])

    st.markdown(f'<div class="box dark-blue-box">📢 <strong>Answer:</strong> {answer}</div>', unsafe_allow_html=True)

    if recommendations:
        st.markdown("🎯 **Laptop Recommendations:**")
        for rec in recommendations:
            st.markdown(f'<div class="box red-box">✔️ {rec["Product Name"]}, {rec["RAM"]},{rec["SSD"]}, {rec["Battery Life"]}, {rec["OS"]}, {rec["Final Price"]}</div>', unsafe_allow_html=True)

    # Provide negotiation tips
    if sentiment in ["Neutral", "Negative"]:
        negotiation_tips = negotiation_coach(st.session_state.conversation)
        st.markdown(f'<div class="box yellow-box">💡 <strong>Negotiation Tips:</strong> {negotiation_tips}</div>', unsafe_allow_html=True)

    time.sleep(4)
    st.session_state.recording = False