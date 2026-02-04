# 100 Days of Python
# Day 31 - Capstone Project
# The Flash Card App

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIME_TO_GUESS = 5000
key = None
timer = None

# Creating the German-to-English dictionary:
data = pandas.read_csv("data/german_words.csv")
data_german = data.German.to_list()
data_english = data.English.to_list()
numbers = [j for j in range(3000)]

# Main functions
def show_german():
    global key
    key = choice(numbers)
    canvas.itemconfig(word_text, text=data_german[key])

def show_english():
    global key
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=data_english[key], fill="white")

def show_word():
    show_german()
    window.after(TIME_TO_GUESS, show_english)

# Word checking function
def wrong_word():
    pass

def right_word():
    pass

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
