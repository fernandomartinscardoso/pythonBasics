"""Speak user generated text using pyttsx3."""

import pyttsx3


def main():
    message = input('What would you like to say? ')
    if message.strip():
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()


if __name__ == '__main__':
    main()
