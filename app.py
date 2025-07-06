import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import platform
import speech_recognition as sr
import av
import webbrowser
import PyPDF2
import requests
from num2words import num2words

# ----------------- Voice Output Setup -----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    st.markdown(f"🎙️ **CHAND:** {text}")
    engine.say(text)
    engine.runAndWait()

# ----------------- Voice Input -----------------
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            st.info("🎧 Listening...")
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                command = self.recognizer.recognize_google(audio).lower()
                st.markdown(f"🗣️ You said: `{command}`")
                run_chand(command)
            except sr.UnknownValueError:
                talk("Sorry, I didn’t catch that.")
            except sr.RequestError:
                talk("Network error.")
        return frame

# ----------------- Command Handler -----------------
def run_chand(command):
    if "chand" in command:
        talk("Yes? I'm listening 👂")

    elif "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "search" in command:
        query = command.replace("search", "").strip()
        talk(f"Searching Google for {query}")
        pywhatkit.search(query)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time} ⏰")

    elif "date" in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk(f"Today is {date} 📅")

    elif "day" in command:
        day = datetime.datetime.now().strftime('%A')
        talk(f"Today is {day} 📆")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find that person.")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif "tell me a fact" in command:
        try:
            res = requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()
            talk(res["text"])
        except:
            talk("Couldn't fetch a fact now 😕")

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome not found 😬")

    elif "open code" in command or "vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "open notepad" in command:
        talk("Opening Notepad 📓")
        os.system("notepad")

    elif "system info" in command:
        info = f"You're running on {platform.system()} {platform.release()} with Python {platform.python_version()}"
        talk(info)

    elif "open downloads" in command:
        path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(path)
        talk("Opening Downloads folder")

    elif "open pictures" in command:
        path = os.path.join(os.path.expanduser("~"), "Pictures")
        os.startfile(path)
        talk("Opening Pictures folder")

    elif "open documents" in command:
        path = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(path)
        talk("Opening Documents")

    elif "read pdf" in command:
        pdf_path = st.text_input("Enter full path of PDF file:")
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = reader.pages[0].extract_text()
                talk("Reading the first page...")
                talk(text[:500])  # Read first 500 characters
        else:
            talk("Please provide a valid path.")

    elif "weather in" in command:
        city = command.replace("weather in", "").strip()
        try:
            url = f"http://wttr.in/{city}?format=3"
            weather = requests.get(url).text
            talk(weather)
        except:
            talk("Couldn't fetch the weather 😞")

    elif "calculate" in command:
        expression = command.replace("calculate", "").strip().replace("plus", "+").replace("minus", "-").replace("into", "*").replace("divided by", "/")
        try:
            result = eval(expression)
            talk(f"The result is {result}")
        except:
            talk("Sorry, I couldn't calculate that.")

    elif "convert" in command and "to words" in command:
        num_str = ''.join(filter(str.isdigit, command))
        try:
            num_word = num2words(int(num_str))
            talk(f"{num_str} in words is: {num_word}")
        except:
            talk("Sorry, couldn't convert number to words.")

    elif "exit" in command or "stop" in command or "bye" in command:
        talk("Goodbye! Shutting down 👋")
        st.stop()

    else:
        talk("I heard you, but Sorry I don’t understand that yet 😅")

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="CHAND Voice Assistant", page_icon="🎤")
st.title("💬 CHAND – Your Personal Voice Assistant")
st.markdown("Say a command using your **microphone**...")

# ----------------- Start Listening -----------------
webrtc_streamer(
    key="chand-assistant",
    audio_receiver_size=1024,
    media_stream_constraints={"audio": True, "video": False},
    audio_processor_factory=AudioProcessor,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
)
