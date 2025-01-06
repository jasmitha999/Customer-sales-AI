import pandas as pd
import os

EXCEL_FILE = "chat_data.xlsx"

def initialize_excel():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=[
            "Date", "Time", "User Input", 
            "Sentiment", "Sentiment Confidence", 
            "Tone", "Tone Confidence", 
            "AI Response"
        ])
        df.to_excel(EXCEL_FILE, index=False)

def save_to_excel(data):
    df = pd.read_excel(EXCEL_FILE)
    new_record = pd.DataFrame([data])
    df = pd.concat([df, new_record], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)
