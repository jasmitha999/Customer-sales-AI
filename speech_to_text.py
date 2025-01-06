import speech_recognition as sr
import streamlit as st
from ai_response import get_ai_response
from text_to_speech import speak_text
from datetime import datetime
from excel_handler import save_to_excel

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                st.write("Listening for your query...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                st.write(f"You said: {text}")
                
                if "stop" in text.lower():
                    st.success("Detected 'stop'. Terminating listening.")
                    break
                
                response, sentiment, sentiment_score, tone, tone_score = get_ai_response(text)
                st.write("### AI Response:")
                st.write(f"{response}")
                st.write(f"Sentiment: {sentiment} (Confidence: {sentiment_score:.2f})")
                st.write(f"Tone: {tone} (Confidence: {tone_score:.2f})")
                
                now = datetime.now()
                data = {
                    "Date": now.strftime("%Y-%m-%d"),
                    "Time": now.strftime("%H:%M:%S"),
                    "User Input": text,
                    "Sentiment": sentiment,
                    "Sentiment Confidence": sentiment_score,
                    "Tone": tone,
                    "Tone Confidence": tone_score,
                    "AI Response": response
                }
                save_to_excel(data)
                
                if st.session_state.get("speech_enabled", True):
                    speak_text(response)
                
            except sr.UnknownValueError:
                st.warning("Sorry, I couldn't understand. Please speak clearly.")
            except sr.RequestError as e:
                st.error(f"Error with the speech recognition service: {e}")
                break
