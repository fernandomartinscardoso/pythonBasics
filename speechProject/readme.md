# Speech Transcription Project

To install Vosk and generate a text transcript from an audio file, you need to install the library, download a language model, and use a Python script to process the audio.
Here is the step-by-step guide to setting it up and outputting a combined, readable transcript.

Step 1: Install Vosk and Dependencies

Open your terminal or command prompt and run the following commands to install the required libraries:

```bash
# Install the core Vosk library
pip install vosk

# Install PyAudio (only needed if you want to transcribe live microphone input)
pip install pyaudio
```

(Note for Linux users: You may need to run `sudo apt install portaudio19-dev` before installing pyaudio.)

Step 2: Download a Vosk Model

Vosk requires a pre-trained language model to recognize speech. [1] (https://www.youtube.com/watch?v=SqVeAxrPAB0&t=501)
1. Head over to the official Vosk Models page.
2. Download a model matching your preferred language. For quick testing in English, the lightweight vosk-model-small-en-us-0.15 (approx. 40MB) is recommended.
3. Extract the downloaded ZIP file into your project directory. Ensure your project folder structure looks like this: [1] (https://www.youtube.com/watch?v=uf5oth4-eF8&t=264), [2] (https://gotranscript.com/public/building-an-offline-digital-assistant-with-vosk-step-by-step-guide), [3] (https://www.youtube.com/watch?v=yHYSwcJaw6c), [4] (https://www.rrjprince.com/2025/07/building-speech-recognition-system-with.html), [5] (https://www.youtube.com/watch?v=SqVeAxrPAB0&t=501)
text
your_project/
├── transcription_script.py
├── test.wav
└── vosk-model-small-en-us-0.15/  <- (The extracted folder containing model files)
Use code with caution.
Important Audio Requirement: Vosk natively processes raw PCM audio. Ensure your audio file is a WAV file formatted as Mono, 16kHz (or 44.1kHz depending on the model), 16-bit PCM. [1] (https://medium.com/@Chirag_writes/from-sound-to-text-building-a-local-ai-assistant-with-vosk-pyaudio-part-1-b9b690eba7c2), [2] (https://www.youtube.com/watch?v=SqVeAxrPAB0&t=501)

Step 3: Python Script to Transcribe and Combine Text

Vosk processes audio in small chunks and outputs partial JSON strings. The script below reads the audio file, passes it to the model, and extracts the individual text snippets to combine them into a single coherent paragraph transcript. [1] (https://medium.com/@Chirag_writes/from-sound-to-text-building-a-local-ai-assistant-with-vosk-pyaudio-part-1-b9b690eba7c2), [2] (https://www.rrjprince.com/2025/07/building-speech-recognition-system-with.html)
Create a file named transcription_script.py and paste the following code:

```python
import os
import sys
import wave
import json
from vosk import Model, KaldiRecognizer

# 1. Define paths
MODEL_PATH = "vosk-model-small-en-us-0.15"  # Change this to your exact model folder name
AUDIO_FILE = "test.wav"                    # Path to your audio file

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
```

## Debugging

In case the code fails and show the issue:

```prompt
LOG (VoskAPI:ReadDataFiles():model.cc:308) Loading winfo vosk-model-small-en-us-0.15/graph/phones/word_boundary.int
Error: Audio file must be MONO (1 channel).
```
The error is caused by `wav` file being stereo. Convert the file to mono using `ffmpeg` and run the script again with the mono file as input:

```bash
ffmpeg -i <filename>.wav -ac 1 -ar 16000 -c:a pcm_s16le <filename>_mono.wav
```

Alternative: The Quick No-Code Method

If you want to quickly combine a model and get a transcript via the command line without writing custom Python code, you can use the built-in CLI utility: [1] (https://alphacephei.com/vosk/install), [2] (https://www.reddit.com/r/speechtech/comments/1qla4zy/struggling_to_install_a_vosk_model_need_guidance/)

```bash
pip install vosk
# This automatically pulls the model and writes the transcript to a text file
vosk-transcriber -n vosk-model-en-us-0.42-gigaspeech -i test.wav -o transcript.txt
```

Next step: add speaker identification (diarization) to separate who said what in the transcript.

## References

[Pytranscript Lib](https://pypi.org/project/pytranscript/)
[Vosk Models](https://alphacephei.com/vosk/models)

