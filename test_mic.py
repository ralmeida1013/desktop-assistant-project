import sounddevice as sd
from scipy.io.wavfile import write

print("Recording... Speak into your microphone")
duration = 5 # seconds
fs = 44100 # sample rate

audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait() # Wait until the recording is finished
write("test.wav", fs, audio_data)
print("Recording complete! Saved as test.wav")