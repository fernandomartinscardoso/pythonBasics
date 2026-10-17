"""Speak the time."""

from datetime import datetime

import pyttsx3


def main():
    spoken_time = datetime.now().strftime('%I %M %p on %A, %B %d, %Y')
    print(spoken_time)

    engine = pyttsx3.init()
    engine.say(spoken_time)
    engine.runAndWait()


if __name__ == '__main__':
    main()
