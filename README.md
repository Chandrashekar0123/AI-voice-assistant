# AI Voice Assistant

A voice-based AI assistant that uses OpenAI's GPT model for natural conversations. Built with Python and Streamlit.

## Features
- Voice input through microphone
- Text-to-speech response using gTTS
- Real-time transcription using Google Speech Recognition
- Conversation history tracking in Streamlit
- Error handling and API key validation
- User-friendly interface with clear instructions

## Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Working microphone
- Internet connection

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chandrashekar0123/AI-voice-assistant.git
   cd AI-voice-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   streamlit run voice_assistant.py
   ```

## Usage
1. Click the "Start Speaking" button
2. Speak clearly into your microphone
3. Wait for the AI's response
4. The response will be both displayed and spoken
5. View your conversation history below

## Troubleshooting
- If the microphone isn't working, check your system's audio input settings
- If you get an API error, verify your OpenAI API key in the `.env` file
- Run `python test_api.py` to verify your API key setup