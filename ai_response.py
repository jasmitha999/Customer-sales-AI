from transformers import pipeline
from api import client
import streamlit as st

# Load Hugging Face pipelines
sentiment_analyzer = pipeline("sentiment-analysis")
tone_classifier = pipeline("zero-shot-classification")

def analyze_sentiment(user_input):
    try:
        result = sentiment_analyzer(user_input)
        sentiment = result[0]["label"]
        score = result[0]["score"]
        return sentiment, score
    except Exception as e:
        st.error(f"Error analyzing sentiment: {e}")
        return "Error", 0.0

def analyze_tone(user_input):
    try:
        labels = ["formal", "casual", "sarcastic", "enthusiastic", "neutral"]
        result = tone_classifier(user_input, candidate_labels=labels)
        tone = result["labels"][0]
        tone_score = result["scores"][0]
        return tone, tone_score
    except Exception as e:
        st.error(f"Error analyzing tone: {e}")
        return "Error", 0.0

def get_ai_response(user_input):
    try:
        sentiment, sentiment_score = analyze_sentiment(user_input)
        tone, tone_score = analyze_tone(user_input)
        
        prompt = f"""User input: {user_input}
        Sentiment: {sentiment} (Confidence: {sentiment_score:.2f})
        Tone: {tone} (Confidence: {tone_score:.2f})
        Provide a concise, relevant response based on the tone and sentiment."""
        
        results = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        response = results.choices[0].message.content.strip()
        return response, sentiment, sentiment_score, tone, tone_score
    except Exception as e:
        st.error(f"Error fetching AI response: {e}")
        return f"Error: {e}", "Error", 0.0, "Error", 0.0
