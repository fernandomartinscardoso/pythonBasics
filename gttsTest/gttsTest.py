from pathlib import Path
from gtts import gTTS

input_file = Path(__file__).with_name("chap2pt-br.txt")
output_file = input_file.with_suffix(".mp3")

text = input_file.read_text(encoding="utf-8-sig").strip()
if not text:
    raise ValueError(f"Text file is empty: {input_file}")

tts = gTTS(text=text, lang="pt", tld="com.br")
tts.save(str(output_file))

print(f"Audio saved to: {output_file}")