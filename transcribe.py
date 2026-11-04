from faster_whisper import WhisperModel

# Load fast local model
model_size = "base"
print("Loading Whisper model...")
model = WhisperModel(model_size, device="cpu", compute_type="int8")

print("Transcribing audio...")
segments, info = model.transcribe("test.wav", beam_size=5)

print(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")

# Print out everything said in the recording
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")