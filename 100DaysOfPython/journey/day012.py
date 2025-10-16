# 100 Days of Python
# Day 12 - Scope
# Project of the day: Number Guessing Game
# Demo link of the game: https://appbrewery.github.io/python-day12-demo/
# ASCII art for the logo: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

import random
from guess_number_art import logo

print(logo)

difficulty_dict = {
    "easy": 10,
    "hard": 5,
}

difficulty_level = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

computer_choice = random.randint(1, 100)

number_of_guesses = 0
while number_of_guesses < difficulty_dict[difficulty_level]:
    number_of_guesses += 1
    remaining_guesses = difficulty_dict[difficulty_level] - number_of_guesses
    guess = int(input("Make a guess: "))
    if guess < computer_choice:
        print("Too low.\nTry again!")
        print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    elif guess > computer_choice:
        print("Too high.\nTry again!")
        print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {computer_choice}.")
        break
    if remaining_guesses == 0:
        print(f"You've run out of options. The answer was {computer_choice}")
