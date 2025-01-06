import streamlit as st
from speech_to_text import transcribe_speech

def main():
    st.title("AI Sales Assistant with Sentiment & Tone Analysis")
    st.write("Simulate a sales conversation. The AI Assistant provides insights into customer sentiment, tone, and objections.")
    
    st.session_state["speech_enabled"] = st.checkbox("Enable Speech Output", value=True)
    
    if st.button("Start Sales Conversation"):
        st.info("AI Sales Assistant is listening. Say 'stop' to terminate.")
        transcribe_speech()

if __name__ == "__main__":
    main()