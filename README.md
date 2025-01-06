AI Sales Assistant with Sentiment & Tone Analysis
Overview
The AI Sales Assistant is a powerful tool designed to assist sales professionals in understanding customer sentiment, analyzing tone, and generating AI-driven suggestions for effective sales communication. The application uses natural language processing (NLP) and speech recognition to analyze customer inputs and provide actionable insights.
Features
•	Sentiment Analysis: Detect customer sentiment using pre-trained NLP models.
•	Tone Analysis: Classify customer tone into categories like interested, hesitant, excited, etc.
•	AI-Generated Suggestions: Receive tailored suggestions based on sentiment and tone.
•	Speech-to-Text Integration: Enable voice input for seamless conversation analysis.
•	Text-to-Speech Output: Get AI responses spoken aloud.
•	Excel Data Logging: Automatically save customer interactions and AI insights into an Excel sheet.
Tech Stack
•	Frontend: Streamlit
•	Backend: Python
•	APIs: Groq API for AI responses
•	Libraries: Transformers, SpeechRecognition, Pyttsx3, Pandas
Installation
Prerequisites
•	Python 3.8+
•	pip
Steps
1.	Clone the repository: 
2.	git clone
3.	cd ai-sales-assistant
4.	Install dependencies: 
5.	pip install -r requirements.txt
6.	Set up the environment variables in a .env file: 
7.	GROQ_API_KEY=your_api_key_here
8.	EXCEL_FILE=sales_data.xlsx
9.	Initialize the Excel file: 
10.	python -c "import excel_handler; excel_handler.initialize_excel()"
11.	Run the Streamlit application: 
12.	streamlit run app.py
Usage
1.	Launch the application via Streamlit.
2.	Enable Speech Output if desired.
3.	Click on Start Sales Conversation.
4.	Speak or type your customer inputs.
5.	View AI insights, sentiment, tone, and suggestions.
6.	Conversations are logged into sales_data.xlsx.
File Structure
•	app.py: Main application entry point.
•	ai_response.py: Handles sentiment and tone analysis.
•	api.py: API client configuration.
•	speech_to_text.py: Manages voice input.
•	text_to_speech.py: Handles AI voice output.
•	excel_handler.py: Manages Excel data storage.
•	requirements.txt: Lists project dependencies.
Environment Variables
•	GROQ_API_KEY: API key for accessing Groq services.
•	EXCEL_FILE: Path to the Excel file for logging.
Contributing
1.	Fork the repository.
2.	Create a new branch: 
3.	git checkout -b feature-branch
4.	Make your changes and commit them.
5.	Push to your branch: 
6.	git push origin feature-branch
7.	Open a pull request.
License
This project is licensed under the GNU License.
Contact
For any questions or support, please reach out via mulejasmitha@gmail.com.
