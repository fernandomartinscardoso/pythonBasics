from pathlib import Path
import re
import subprocess
from tempfile import NamedTemporaryFile

import imageio_ffmpeg
import pyttsx3


INPUT_FILE = Path(__file__).with_name("<file_name>.txt")
OUTPUT_FILE = Path(__file__).with_name("<file_name>.mp3")
SPEECH_RATE = 150


def main() -> None:
    if not INPUT_FILE.is_file():
        raise FileNotFoundError(f"Text file not found: {INPUT_FILE}")

    text = INPUT_FILE.read_text(encoding="utf-8-sig").strip()
    if not text:
        raise ValueError(f"Text file is empty: {INPUT_FILE}")

    engine = pyttsx3.init()
    engine.setProperty("rate", SPEECH_RATE)

    english_voice = None
    for voice in engine.getProperty("voices"):
        details = " ".join(
            [
                voice.id,
                voice.name,
                *[
                    language.decode(errors="ignore")
                    if isinstance(language, bytes)
                    else str(language)
                    for language in getattr(voice, "languages", [])
                ],
            ]
        )
        if "english" in details.casefold() or re.search(
            r"(^|[^a-z])en(?:$|[-_])", details, re.IGNORECASE
        ):
            english_voice = voice
            break

    if english_voice is None:
        raise RuntimeError(
            "No English Windows speech voice is installed. Add an English "
            "voice in Windows Settings > Time & language > Speech."
        )

    engine.setProperty("voice", english_voice.id)
    with NamedTemporaryFile(
        dir=OUTPUT_FILE.parent, suffix=".wav", delete=False
    ) as wav_file:
        wav_path = Path(wav_file.name)
    with NamedTemporaryFile(
        dir=OUTPUT_FILE.parent, suffix=".mp3", delete=False
    ) as mp3_file:
        mp3_path = Path(mp3_file.name)

    try:
        engine.save_to_file(text, str(wav_path))
        engine.runAndWait()
        if not wav_path.is_file() or wav_path.stat().st_size == 0:
            raise RuntimeError("Windows speech engine did not create the WAV audio.")

        subprocess.run(
            [
                imageio_ffmpeg.get_ffmpeg_exe(),
                "-y",
                "-i",
                str(wav_path),
                "-codec:a",
                "libmp3lame",
                "-qscale:a",
                "2",
                str(mp3_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        if not mp3_path.is_file() or mp3_path.stat().st_size == 0:
            raise RuntimeError("MP3 encoder did not create the audio file.")
        mp3_path.replace(OUTPUT_FILE)
    except subprocess.CalledProcessError as error:
        message = error.stderr.strip() or str(error)
        raise RuntimeError(f"Could not encode MP3 audio: {message}") from error
    finally:
        wav_path.unlink(missing_ok=True)
        mp3_path.unlink(missing_ok=True)

    print(f"Audio saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
