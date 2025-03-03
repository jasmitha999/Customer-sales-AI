# InfosysSpringboard5.0-Group1
# Real-Time AI-Powered Sales Intelligence Tool

# Introduction

The Real-Time AI-Powered Sales Intelligence Tool is designed to revolutionize live sales calls by providing actionable insights and suggestions to sales teams in real-time. This cutting-edge tool leverages 
advanced AI models for sentiment and intent analysis, integrates with CRM data and Google Sheets, and provides optimized negotiation strategies to enhance customer engagement and drive sales outcomes.

## Features

Real-time Speech Recognition for continuous audio recording from the buyer. 

Automated Speech-to-Text Transcription to convert recorded audio into text.

Sentiment and Intent Analysis powered by state-of-the-art NLP models.

Recommending Laptops based on the given input.

Intelligent Negotiation Terms Generation based on buyer sentiment and intent.

Seamless Google Sheets Integration to record and manage buyer interactions.

Fully functional Workflow Integration to streamline processes end-to-end.

## Project Workflow

The project workflow includes 8 major steps:

# 1. Speech Recognition

Tools Used: PyAudio, SpeechRecognition libraries.

Functionality: Continuously records audio input from the buyer during live sales calls.

# 2. Transcription of Recorded Audio

API: Google Speech-to-Text API.

Implementation:Enabled Google Drive and Google Sheets APIs.

Downloaded credentials.json file using a service account on Google Console.

Output: Converts audio into text for further processing.

# 3. Sentiment and Intent Analysis

Models Used:Sentiment Analysis: cardiffnlp/twitter-roberta-base-sentiment from Hugging Face.

Intent Analysis: facebook/bart-large-mnli from Hugging Face.

Objective: Understand the buyer's mood and intent to provide actionable insights.

# 4. Deal Recommendations

Models used: Command-xlarge-nightly model from Cohere LLM

Approach: Suggest laptops based on the input given by the buyer and extract matched laptops names in the input to the product name in the dataset, recommends to the buyer.

# 5. Negotiating Terms Generation

Models used: Command-xlarge-nightly model from Cohere LLM

Approach: Extracts keywords based on sentiment and intent analysis.

Generates basic negotiation terms tailored to the buyer's context.

# 6. Summarization of Conversation

Aprroach: Summarizes the whole conversation and finalises the deal status based on the sentiment.

Model used: llama 3.3 70b versatile model from GROQ LLM.

# 7. Google Sheets Integration

Purpose: Records all buyer interactions and contextual data for tracking and analysis.

Implementation:Used the spreadsheet ID of a shared Google Sheet linked with the service account in the credentials file.

# 8. Workflow Integration
Objective: Seamlessly integrates all steps into a unified, functional workflow for real-time operation.

## Contribution Guidelines

We welcome contributions to enhance this project. Please follow the guidelines below:

## Reporting Issues

Check existing issues before creating a new one.

Provide a clear and concise description of the problem. Include steps to reproduce the issue, if applicable.

## Making Changes

Fork the Repository: Create your own fork of the repository.

Clone the Repository: Clone the forked repository to your local machine.

git clone https://github.com/Joshithach18/InfosysSpringboard5.0-Group1.git

Create a Branch: Create a new branch for your changes.

git checkout -b feature/your-feature-name

Commit Changes: Commit your changes with a descriptive message.

git commit -m "Add description of your changes"

Push Changes: Push your changes to your forked repository.

git push origin feature/your-feature-name

Create a Pull Request: Submit a pull request to the main repository.

## Code Standards

Follow PEP 8 for Python code.

Include comments and documentation for clarity.

Write unit tests where applicable.

## Additional Contributions

Enhance existing features.

Optimize performance.

Integrate additional NLP or AI models for improved accuracy.

## License
By contributing, you agree that your contributions will be licensed under the same license as the project.

## Getting Started

Clone the repository:

git clone https://github.com/Joshithach18/InfosysSpringboard5.0-Group1.git

cd InfosysSpringboard5.0-Group1

## Install required dependencies:

pip install -r requirements.txt

Run the project:

Streamlit run frontend.py

## Acknowledgments

This project uses:

Hugging Face Transformers

Cohere LLM

Groq LLM

Google Speech-to-Text API

Google Sheets API

#### Previous Intercation summary spreadsheet URL: https://docs.google.com/spreadsheets/d/1BQRX513_GAiLKokObbJoA30foTKzLC_BFS48LD5MMTM/edit?gid=0#gid=0

#### Presentation file: https://docs.google.com/presentation/d/1uLfUlGXl_pjd5aujuCsOyt5ukJWSQjP-/edit?usp=sharing&ouid=115290809046251519926&rtpof=true&sd=true

#### Demo Video: https://drive.google.com/file/d/1F5uPjfG2CPpY79v2WGxCtKF0jKx-1GP7/view?usp=sharing

### This project is done in collaboration of the first group of three of us, as part of our Internship at Infosys Springboard 5.0

### Contirbutors:

### Mule Jasmitha Reddy (Email:21204031@rmd.ac.in,Github repo:https://github.com/jasmitha999/Customer-sales-AI)

### Nitisha Choudary (Email:choudharynitisha00@gmail.com,Github repo:https://github.com/NitishaChoudhary/Internship-Infosys5.0B3)

### Joshitha Chennamsetty (Email:joshithachennamsetty@gmail.com,Github repo:https://github.com/Joshithach18/Infosys-Springboard-5.0-internship)
