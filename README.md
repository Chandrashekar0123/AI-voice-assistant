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

```
##  CHAND Voice Assistant – Commands and Actions
```
| **Voice Command**           | **Action Performed**                                                        |
| --------------------------- | --------------------------------------------------------------------------- |
| `chand`                     | Responds with "Yes? I'm listening 👂"                                       |
| `play <song name>`          | Plays the song on YouTube using **pywhatkit.playonyt()**                    |
| `search <query>`            | Searches Google with the query using **pywhatkit.search()**                 |
| `time`                      | Speaks the **current time** in `HH:MM AM/PM` format                         |
| `date`                      | Speaks the **current date** (e.g., July 27, 2025)                           |
| `day`                       | Speaks the **current weekday** (e.g., Sunday)                               |
| `who is <person>`           | Reads the first sentence of the person’s Wikipedia summary                  |
| `joke`                      | Tells a random **programming joke** using **pyjokes**                       |
| `tell me a fact`            | Fetches a **random useless fact** from the `uselessfacts.jsph.pl` API       |
| `open chrome`               | Opens **Google Chrome**, if path exists locally                             |
| `open code` or `vs code`    | Launches **Visual Studio Code** using `os.system("code")`                   |
| `open notepad`              | Opens **Notepad** application on Windows                                    |
| `system info`               | Speaks OS name, release version, and Python version                         |
| `open downloads`            | Opens the **Downloads** folder using `os.startfile()`                       |
| `open pictures`             | Opens the **Pictures** folder                                               |
| `open documents`            | Opens the **Documents** folder                                              |
| `read pdf`                  | Prompts for a **PDF path**, reads & speaks first 500 characters of page 1   |
| `weather in <city>`         | Fetches and speaks **current weather** using `wttr.in` API                  |
| `calculate <expression>`    | Evaluates math expressions (supports `plus`, `minus`, `into`, `divided by`) |
| `convert <number> to words` | Converts number to **English words** using `num2words()`                    |
| `exit` / `stop` / `bye`     | Ends the assistant session with a goodbye message                           |
| *(any other input)*         | Replies with "Sorry I don’t understand that yet 😅"                         |

---


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
