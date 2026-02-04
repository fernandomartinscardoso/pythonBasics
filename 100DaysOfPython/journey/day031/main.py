# 100 Days of Python
# Day 31 - Capstone Project
# The Flash Card App

from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIME_TO_GUESS = 5000
key = ""
word_counter = 0
right_counter = 0
wrong_counter = 0

# Creating the German-to-English dictionary:
data = pandas.read_csv("data/german_words.csv")
data_german = data.German.to_list()
data_english = data.English.to_list()
de_en_dictionary = {data_german[i]:data_english[i] for i in range(len(data_german))}

# Main functions
def show_german():
    global key
    key = choice(data_german)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(language_text, text="Deutsch", fill="black")
    canvas.itemconfig(word_text, text=key, fill="black")

def show_english():
    global key
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=de_en_dictionary[key], fill="white")

def show_word():
    show_german()
    window.after(TIME_TO_GUESS, show_english)

def save_progress():
    global word_counter, wrong_counter, right_counter
    with open("my_progress.txt", mode="w") as file:
        file.write(f"Total words: {word_counter}\n")
        file.write(f"Total right: {right_counter}\n")
        file.write(f"Total wrong: {wrong_counter}")

# Word checking functions
def wrong_word():
    global word_counter, wrong_counter
    word_counter += 1
    wrong_counter += 1
    save_progress()
    show_word()

def right_word():
    global word_counter, right_counter
    word_counter += 1
    right_counter += 1
    save_progress()
    show_word()

# Window setup
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=900, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(450, 273, image=card_front_image)
language_text = canvas.create_text(450, 170, text="Deutsch", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(450, 300, text=key, fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_word_button = Button(image=wrong_button_image, highlightthickness=0, command=wrong_word)
wrong_word_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
wrong_word_button = Button(image=right_button_image, highlightthickness=0, command=right_word)
wrong_word_button.grid(column=1, row=1)

show_word()

window.mainloop()
