import time
import pyaudio
import wave
import speech_recognition as sr
from transformers import pipeline
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import re
import streamlit as st
import cohere

COHERE_API_KEY = "wnDl2gFhkWSgehGd193dsPfVMKIJlDaSooLiXJrp"
co = cohere.Client(COHERE_API_KEY)
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

laptop_data = pd.read_csv("laptop_dataset_updated.csv")
customer_history_path = "dataset_preparation - Sheet1.csv"
customer_history = pd.read_csv(customer_history_path)

def initialize_google_sheets(credentials_path):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    return gspread.authorize(credentials)

def get_speech_input():
    recognizer = sr.Recognizer()
    combined_text = ""
    with sr.Microphone() as source:
        st.info("Listening... Please speak now. Say 'stop' to end.")
        while True:
            try:
                audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = recognizer.recognize_google(audio_data).lower()
                if "stop" in text:
                    st.info("Stopping input as 'stop' was detected.")
                    break
                combined_text += text + " "
                st.write(f"You said: {text}")
            except sr.WaitTimeoutError:
                st.warning("Listening timed out. Please try again.")
            except sr.UnknownValueError:
                st.warning("Sorry, I could not understand the audio. Please try again.")
            except sr.RequestError as e:
                st.error(f"Could not request results; {e}")
                break
    return combined_text.strip()

def summarize_input(user_input):
    try:
        response = co.generate(
            model="summarize-xlarge",
            prompt=f"Summarize the following input into a single concise sentence:\n{user_input}",
            max_tokens=100,
            temperature=0.5,
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"Error with Cohere summarization: {e}")
        return "Error generating summary."

def generate_bullet_points(text):
    lines = text.split("\n")
    bullet_points = "\n".join([f"• {line.strip()}" for line in lines if line.strip()])
    return bullet_points

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    sentiment = result[0]["label"]
    return "Positive" if sentiment == "LABEL_2" else ("Neutral" if sentiment == "LABEL_1" else "Negative")

def filter_laptops(user_input):
    user_input_lower = user_input.lower()
    budget = None

    if "under" in user_input_lower:
        budget_matches = re.findall(r"under\s+(\d+)", user_input_lower)
        budget = int(budget_matches[0]) if budget_matches else None

    filtered_data = laptop_data.copy()
    if budget:
        filtered_data = filtered_data[filtered_data["Final Price"] <= budget]
    return filtered_data

def get_general_recommendations():
    general_recommendations = laptop_data.head(3)
    recommendations = []

    for _, row in general_recommendations.iterrows():
        recommendations.append(
            f"- Brand & Model: {row['Product Name']}\n"
            f"  - Price: Rs.{row['Final Price']}\n"
            f"  - Specifications: {row['RAM']}GB RAM, {row['SSD (GB)']}GB SSD, {row['HDD (GB)']}GB HDD\n"
            f"  - Battery Life: {row['Battery Life (hrs)']} hrs, Graphics Card: {row['Graphics Card']}\n"
            f"  - CPU: {row['CPU']}, OS: {row['OS']}, Screen: {row['Screen Size (inches)']} inches\n"
            f"  - Screen Technology: {row['Screen Technology']}, Resolution: {row['Resolution']}\n"
            f"  - Discount: {row['Discount (%)']}%, Deals: {row['Deals']}\n"
        )

    return "\n\n".join(recommendations)

def find_customer_row(sheet, customer_name):
    data = sheet.get_all_values()
    for index, row in enumerate(data):
        if row and row[0].strip().lower() == customer_name.strip().lower():
            return index + 1
    return None

def append_customer_interaction(sheet, customer_name, interaction, summary, sentiment, deal_status):
    row_index = find_customer_row(sheet, customer_name)
    column_headers = sheet.row_values(1)

    if row_index:
        existing_row = sheet.row_values(row_index)
        num_interactions = (len(existing_row) - 1) // 4
        next_column_start = 2 + num_interactions * 4

        headers_to_add = [
            f"Interaction {num_interactions + 1}",
            f"Summary {num_interactions + 1}",
            f"Sentiment {num_interactions + 1}",
            f"Deal Status {num_interactions + 1}"
        ]

        for i, header in enumerate(headers_to_add):
            if len(column_headers) < next_column_start + i:
                sheet.update_cell(1, next_column_start + i, header)

        new_data = [interaction, summary, sentiment, deal_status]
        for i, value in enumerate(new_data):
            sheet.update_cell(row_index, next_column_start + i, value)
    else:
        new_row = [customer_name, interaction, summary, sentiment, deal_status]
        sheet.append_row(new_row)

def generate_recommendations(sheet, user_input, customer_name):
    try:
        customer_row_index = find_customer_row(sheet, customer_name)

        if customer_row_index:
            row_data = sheet.row_values(customer_row_index)
            st.write("### Past Interactions:")
            for i in range(1, len(row_data), 4):
                if i + 3 < len(row_data):
                    st.write(f"- Interaction: {row_data[i]}\n  - Summary: {row_data[i + 1]}\n  - Sentiment: {row_data[i + 2]}\n  - Deal Status: {row_data[i + 3]}")

            if len(row_data) > 4:  # Ensure enough columns are present
                deal_status = row_data[4]
            else:
                deal_status = "not closed"

            if deal_status == "closed":
                filtered_data = filter_laptops(user_input)
            else:
                summary = summarize_input(user_input)  # Use Cohere to summarize input
                filtered_data = filter_laptops(summary)
        else:
            # New customer or no data found for the customer
            summary = summarize_input(user_input)  # Use Cohere to summarize input
            filtered_data = filter_laptops(summary)

        if filtered_data.empty:
            return "No laptops match your criteria."

        response = co.generate(
            model="command-xlarge",
            prompt=(f"User Input: {user_input}\n Generate a single concise and helpful recommendation."),
            max_tokens=200,
            temperature=0.7,
        )

        enriched_recommendations = response.generations[0].text.strip()
        return generate_bullet_points(enriched_recommendations)

    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return "An error occurred while generating recommendations. Please try again later."

def main():
    st.title("Integrated Customer & Recommendation System")

    credentials_path = "credentials.json"
    spreadsheet_id = "1UPPDEfSS8QMuFzPYPuVvTs2Ai3ffu1W49n-1ROqvPhA"
    sheets_client = initialize_google_sheets(credentials_path)
    sheet = sheets_client.open_by_key(spreadsheet_id).sheet1

    user_name = st.text_input("Enter your name:")

    st.write("Press the button below and speak your laptop requirements. Say 'stop' to finish.")

    if st.button("Record Requirements"):
        user_input = get_speech_input()
        if user_input:
            st.write(f"Final input: {user_input}")

            if user_name and user_input:
                summary = summarize_input(user_input)
                recommendations = generate_recommendations(sheet, user_input, user_name)
                st.write("### Recommendations")
                st.text(recommendations)

                sentiment = analyze_sentiment(user_input)

                if sentiment == "Positive":
                    deal_status = "closed"
                elif sentiment == "Neutral":
                    deal_status = "not closed"
                else:
                    deal_status = "not closed"

                append_customer_interaction(sheet, user_name, user_input, summary, sentiment, deal_status)

                st.success("Interaction logged and recommendations displayed.")
            elif not user_name:
                st.warning("Please provide your name. Showing general recommendations for new users.")
                general_recommendations = get_general_recommendations()
                st.write("### General Recommendations")
                st.text(general_recommendations)
            else:
                st.warning("Please fill in all fields.")

    user_input = st.text_input("Enter your laptop requirements:")

    if st.button("Get Recommendations"):
        if not user_name.strip() or not user_input.strip():
            st.warning("Please provide both your name and your laptop requirements.")
        else:
            st.write(f"Final input: {user_input}")

            if user_name and user_input:
                summary = summarize_input(user_input)
                recommendations = generate_recommendations(sheet, user_input, user_name)
                st.write("### Recommendations")
                st.text(recommendations)

                sentiment = analyze_sentiment(user_input)

                if sentiment == "Positive":
                    deal_status = "closed"
                elif sentiment == "Neutral":
                    deal_status = "not closed"
                else:
                    deal_status = "not closed"

                append_customer_interaction(sheet, user_name, user_input, summary, sentiment, deal_status)

                st.success("Interaction logged and recommendations displayed.")
            elif not user_name:
                st.warning("Please provide your name. Showing general recommendations for new users.")
                general_recommendations = get_general_recommendations()
                st.write("### General Recommendations")
                st.text(general_recommendations)
            else:
                st.warning("Please fill in all fields.")

if __name__ == "__main__":
    main()
