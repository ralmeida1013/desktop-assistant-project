import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import ollama
import pyttsx3
import subprocess
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def open_discord():
    user_profile = os.environ.get("USERPROFILE")
    discord_path = os.path.join(
        user_profile, "AppData", "Local", "Discord", "Update.exe"
    )

    if os.path.exists(discord_path):
        # Launch Discord using update loader
        subprocess.Popen([discord_path, "--processStart", "Discord.exe"])
        return "Opening Discord for you, sir."
    else:
        return "I couldn't find Discord installed on your system, sir."

# Listen and record
print("Listening...")
duration = 5
fs = 44100
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
write("input.wav", fs, audio_data)
print("Recording finished. Transcribing...")

# Transcribe audio
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe("input.wav")
user_text = "".join([segment.text for segment in segments])
print(f"You said: {user_text}")

# Think with Ollama
print("Thinking...")
if "load up the gamer zone" in user_text.lower():
    response_text = open_discord()
    speak(response_text)
else:
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a concise and witty desktop assistant like the AI from the Marvel Cinematic Universe."
                    "Keep your answers under two sentences."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )
    speak(response["message"]["content"])