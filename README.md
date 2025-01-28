Real-Time AI Sales Intelligence and Sentiment-Driven Deal Negotiation Assistant
Overview
The Real-Time AI-Powered Sales Intelligence Tool is a cutting-edge solution designed to revolutionize live sales interactions. It provides actionable insights, real-time negotiation strategies, and seamless data management, ensuring improved customer engagement and optimized sales outcomes.

Key Features
Real-Time Speech Recognition: Captures live audio input from sales calls.
Automated Transcription: Converts audio into text for further analysis.
Sentiment and Intent Analysis: Leverages advanced NLP models to assess customer emotions and intent.
Dynamic Negotiation Terms: Generates optimized terms based on buyer context.
Deal Recommendations: Matches buyer needs with relevant products.
Conversation Summarization: Summarizes calls and determines deal status.
Google Sheets Integration: Logs buyer interactions for analysis and reporting.
Tech Stack
Frontend: Streamlit
Backend: Python
APIs: Google Speech-to-Text, Google Sheets API
Libraries: Hugging Face Transformers, SpeechRecognition, Pandas
Installation
Prerequisites
Python 3.10+
pip
Steps
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/your-username/real-time-ai-sales-intelligence.git
cd real-time-ai-sales-intelligence
Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the project root:
makefile
Copy
Edit
GOOGLE_CREDENTIALS_PATH=path_to_credentials.json
SHEET_ID=your_google_sheet_id
Run the Application:
bash
Copy
Edit
python main.py
Workflow
Speech Recognition:
Captures real-time audio input during sales calls.

Audio Transcription:
Utilizes Google Speech-to-Text API to convert audio into text.

Sentiment and Intent Analysis:
Models:

Sentiment Analysis: cardiffnlp/twitter-roberta-base-sentiment
Intent Analysis: facebook/bart-large-mnli
Objective: Understand customer sentiment and intent to provide actionable insights.
Deal Recommendations:
Matches buyer inputs with relevant product suggestions from a predefined dataset.

Negotiation Terms:
Generates customized negotiation strategies based on sentiment and intent analysis.

Conversation Summarization:
Summarizes the interaction and provides deal status insights.
Model: llama 3.3 70b versatile model

Google Sheets Logging:
Logs interactions, insights, and deal summaries into a shared Google Sheet for tracking.

File Structure
app.py: Main application file for Streamlit interface.
ai_models.py: Handles sentiment and intent analysis.
speech_processing.py: Converts speech input to text and vice versa.
negotiation.py: Generates negotiation terms.
data_logger.py: Logs data into Google Sheets.
requirements.txt: Lists all required libraries and dependencies.
.env: Stores environment variables securely.
Contributing
Steps to Contribute:
Fork the repository.
Clone your fork:
bash
Copy
Edit
git clone https://github.com/your-username/real-time-ai-sales-intelligence.git
Create a branch for your feature:
bash
Copy
Edit
git checkout -b feature/your-feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Add your feature description"
Push your branch:
bash
Copy
Edit
git push origin feature/your-feature-name
Submit a pull request.
Guidelines
Follow PEP 8 coding standards.
Write clear comments and documentation.
Add tests for new features.
License
This project is licensed under the GNU License. By contributing, you agree that your work will be licensed under the same terms.

Contact
For any questions or feedback, feel free to reach out at:
Email: mulejasmithareddy@gmail.com
