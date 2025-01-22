Customer Sales AI

Overview

Customer Sales AI is a powerful tool designed to assist sales professionals by leveraging artificial intelligence for sentiment analysis, tone detection, and generating AI-driven suggestions for effective communication. This application uses natural language processing (NLP) and speech recognition to analyze customer inputs and provide actionable insights.

Features

- **Sentiment Analysis**: Detect customer sentiment using pre-trained NLP models.
- **Tone Analysis**: Classify customer tone into categories like interested, hesitant, excited, etc.
- **AI-Generated Suggestions**: Receive tailored suggestions based on sentiment and tone.
- **Speech-to-Text Integration**: Enable voice input for seamless conversation analysis.
- **Text-to-Speech Output**: Get AI responses spoken aloud.
- **Excel Data Logging**: Automatically save customer interactions and AI insights into an Excel sheet.

Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**: Custom AI modules
- **Libraries**: Transformers, SpeechRecognition, Pyttsx3, Pandas

Installation

Prerequisites

- Python 3.10+
- pip

Steps

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd infosys_project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables in a `.env` file:

   ```env
   API_KEY=your_api_key_here
   EXCEL_FILE=sales_data.xlsx
   ```

4. Initialize the Excel file:

   ```bash
   python -c "import excel_handler; excel_handler.initialize_excel()"
   ```

5. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

Usage

1. Launch the application via Streamlit.
2. Enable Speech Output if desired.
3. Click on Start Sales Conversation.
4. Speak or type your customer inputs.
5. View AI insights, sentiment, tone, and suggestions.
6. Conversations are logged into `sales_data.xlsx`.

File Structure

- **`app.py`**: Main application entry point for running the Streamlit application.
- **`ai_response.py`**: Handles sentiment and tone analysis using pre-trained models.
- **`api.py`**: Configures API interactions and manages requests to external AI services.
- **`speech_to_text.py`**: Manages voice input processing and converts speech to text.
- **`text_to_speech.py`**: Converts AI-generated text responses into speech output.
- **`excel_handler.py`**: Handles data logging and storage in the Excel file.
- **`unified.py`**: Integrates various modules to ensure cohesive functionality.
- **`requirements.txt`**: Lists all dependencies and libraries required for the project.
- **`.env`**: Contains environment variables for secure API key and file path configurations.

Environment Variables

- **`API_KEY`**: API key for accessing AI services.
- **`EXCEL_FILE`**: Path to the Excel file for logging.

Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them.
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

License

This project is licensed under the GNU License.

Contact

For any questions or support, please reach out via [mulejasmithareddy@gmail.com](mailto\:mulejasmithareddy@gmail.com).
