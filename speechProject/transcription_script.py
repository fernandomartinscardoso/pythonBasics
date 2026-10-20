import os
import sys
import wave
import json
from vosk import Model, KaldiRecognizer

# 1. Define paths
MODEL_PATH = "vosk-model-small-en-us-0.15"  # Change this to your exact model folder name
AUDIO_FILE = "<filename>_mono.wav"                    # Path to your audio file

if not os.path.exists(MODEL_PATH):
    print(f"Error: Model directory '{MODEL_PATH}' not found. Please download and extract it.")
    sys.exit(1)

if not os.path.exists(AUDIO_FILE):
    print(f"Error: Audio file '{AUDIO_FILE}' not found.")
    sys.exit(1)

# 2. Load the model and initialize the recognizer
print("Loading model...")
model = Model(MODEL_PATH)

# Open the audio file to inspect its properties
wf = wave.open(AUDIO_FILE, "rb")
if wf.getnchannels() != 1:
    print("Error: Audio file must be MONO (1 channel).")
    sys.exit(1)

# Initialize the recognizer with the correct frame rate matching the audio file
recognizer = KaldiRecognizer(model, wf.getframerate())
recognizer.SetWords(True)  # Optional: enables word-level timestamps inside the JSON if needed

# 3. Process the audio chunks and combine into a final transcript
print("Transcribing audio...")
transcript_fragments = []

while True:
    data = wf.readframes(4000)  # Read audio in 4000-frame chunks
    if len(data) == 0:
        break
    
    if recognizer.AcceptWaveform(data):
        # Result contains a finalized chunk of text
        result_dict = json.loads(recognizer.Result())
        if "text" in result_dict and result_dict["text"] != "":
            transcript_fragments.append(result_dict["text"])

# Catch the remaining text at the very end of the file
final_result = json.loads(recognizer.FinalResult())
if "text" in final_result and final_result["text"] != "":
    transcript_fragments.append(final_result["text"])

wf.close()

# 4. Combine all fragments into a single string
full_transcript = " ".join(transcript_fragments)

# Print and save the combined transcript
print("\n--- Transcription Completed ---")
print(full_transcript)

with open("transcript.txt", "w") as f:
    f.write(full_transcript)
print("\nTranscript successfully saved to 'transcript.txt'.")
