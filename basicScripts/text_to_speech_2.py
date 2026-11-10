import argparse
from pathlib import Path
import re
import subprocess
import threading
from tempfile import TemporaryDirectory

import imageio_ffmpeg
import pyttsx3


DEFAULT_INPUT_FILE = Path(__file__).with_name("<file_name>.txt")
DEFAULT_LANGUAGE = "de-DE"
SPEECH_RATE = 150
MAX_SYNTHESIS_CHARS = 4000
SYNTHESIS_TIMEOUT_SECONDS = 120
LANGUAGE_TAG_PATTERN = re.compile(r"^[a-z]{2,3}(?:-[a-z0-9]{2,8})*$", re.IGNORECASE)


def _normalize_language(value: str) -> str:
    value = re.sub(r"^[^a-z0-9]+", "", value.strip().casefold())
    return value.replace("_", "-")


def _voice_matches_language(voice: object, language: str) -> bool:
    voice_id = str(getattr(voice, "id", ""))
    voice_name = str(getattr(voice, "name", ""))
    languages = getattr(voice, "languages", []) or []
    language_values = [
        item.decode(errors="ignore") if isinstance(item, bytes) else str(item)
        for item in languages
    ]
    normalized_language = _normalize_language(language)
    normalized_values = [_normalize_language(value) for value in language_values]

    if normalized_language == "pt-br":
        details = f"{voice_id} {voice_name}".casefold().replace("_", "-")
        if any(marker in details for marker in ("pt-br", "ptbr", "brazil", "brasileir")):
            return True

    for voice_language in normalized_values:
        if voice_language == normalized_language:
            return True
        if normalized_language == "pt-br":
            continue
        if voice_language == normalized_language.split("-", maxsplit=1)[0]:
            return True
        if (
            "-" not in normalized_language
            and voice_language.startswith(f"{normalized_language}-")
        ):
            return True

    if normalized_language.startswith("de"):
        details = f"{voice_id} {voice_name}".casefold()
        return "german" in details or "deutsch" in details
    return False


def _select_voice(voices: list[object], language: str) -> object:
    for voice in voices:
        if _voice_matches_language(voice, language):
            return voice

    available = ", ".join(
        f"{getattr(voice, 'name', 'Unknown')} ({getattr(voice, 'id', 'unknown')})"
        for voice in voices
    )
    if not available:
        available = "none"
    raise RuntimeError(
        f"No speech voice matching '{language}' is installed. "
        f"Available voices: {available}. Install a matching system voice and try again."
    )


def _split_text(text: str) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + MAX_SYNTHESIS_CHARS, len(text))
        if end < len(text):
            whitespace = list(re.finditer(r"\s+", text[start:end]))
            if whitespace:
                end = start + whitespace[-1].end()
        chunks.append(text[start:end])
        start = end
    return chunks


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a UTF-8 text file to speech using an installed voice."
    )
    parser.add_argument(
        "--language",
        default=DEFAULT_LANGUAGE,
        help="Voice language/locale (for example: de-DE or pt-BR; default: de-DE).",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_FILE,
        help="UTF-8 text input file (default: <file_name>.txt beside this script).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="MP3 output file (default: input file with an .mp3 extension).",
    )
    args = parser.parse_args()
    if not LANGUAGE_TAG_PATTERN.fullmatch(args.language):
        parser.error("--language must be a language code such as 'de' or locale such as 'pt-BR'.")
    if args.output is None:
        args.output = args.input.with_suffix(".mp3")
    return args


def main() -> None:
    args = _parse_args()
    if not args.input.is_file():
        raise FileNotFoundError(f"Text file not found: {args.input}")

    text = args.input.read_text(encoding="utf-8-sig").strip()
    if not text:
        raise ValueError(f"Text file is empty: {args.input}")

    engine = pyttsx3.init()
    engine.setProperty("rate", SPEECH_RATE)
    voice = _select_voice(engine.getProperty("voices"), args.language)
    engine.setProperty("voice", getattr(voice, "id"))
    synthesis_finished = threading.Event()
    synthesis_completed = []

    def on_synthesis_finished(name: str, completed: bool) -> None:
        synthesis_completed.append(completed)
        synthesis_finished.set()

    engine.connect("finished-utterance", on_synthesis_finished)

    try:
        with TemporaryDirectory(dir=args.output.parent, prefix=".tts-") as temp_dir:
            temp_path = Path(temp_dir)
            wav_paths = []
            for index, chunk in enumerate(_split_text(text)):
                chunk = chunk.strip()
                if not chunk:
                    continue
                wav_path = temp_path / f"chunk_{index:04}.wav"
                synthesis_finished.clear()
                synthesis_completed.clear()
                engine.save_to_file(chunk, str(wav_path))
                engine.runAndWait()
                if not synthesis_finished.wait(SYNTHESIS_TIMEOUT_SECONDS):
                    raise TimeoutError(
                        f"Speech engine did not finish chunk {index + 1} within "
                        f"{SYNTHESIS_TIMEOUT_SECONDS} seconds."
                    )
                if not synthesis_completed[-1]:
                    raise RuntimeError(
                        f"Speech engine did not complete chunk {index + 1}."
                    )
                if not wav_path.is_file() or wav_path.stat().st_size == 0:
                    raise RuntimeError(
                        f"Speech engine did not create WAV audio for chunk {index + 1}."
                    )
                wav_paths.append(wav_path)

            concat_file = temp_path / "audio.txt"
            concat_file.write_text(
                "".join(f"file '{wav_path.name}'\n" for wav_path in wav_paths),
                encoding="utf-8",
            )
            mp3_path = temp_path / "audio.mp3"
            subprocess.run(
                [
                    imageio_ffmpeg.get_ffmpeg_exe(),
                    "-y",
                    "-f",
                    "concat",
                    "-i",
                    str(concat_file),
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
            mp3_path.replace(args.output)
    except subprocess.CalledProcessError as error:
        message = (error.stderr or "").strip() or str(error)
        raise RuntimeError(f"Could not encode MP3 audio: {message}") from error

    print(f"Audio saved to: {args.output}")


if __name__ == "__main__":
    main()
