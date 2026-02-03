# 100 Days of Python
# Day 31 - Capstone Project
# The Flash Card App

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pandas
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIME_TO_GUESS = 5

# Creating the German-to-English dictionary:
data = pandas.read_csv("data/german_words.csv")
data_german = data.German.to_list()
data_english = data.English.to_list()
de_en_dict = {data_german[i]: data_english[i] for i in range(len(data_german))}

# Count down function:
timer = None
def count_down(count):
    global timer
    timer = window.after(1000, count_down, count-1)

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
canvas.create_image(450, 273, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_word_button = Button(image=wrong_button_image, highlightthickness=0, command=wrong_word)
wrong_word_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
wrong_word_button = Button(image=right_button_image, highlightthickness=0, command=right_word)
wrong_word_button.grid(column=1, row=1)

# Labels
def show_german():
    key = choice(data_german)
    language_label = Label(text="Deutsch", font=(FONT_NAME, 40, "italic"), bg="white")
    language_label.place(x=350, y=100)

    word_label = Label(text=key, font=(FONT_NAME, 60, "bold"), bg="white")
    word_label.place(x=350-10*len(key), y=213)

show_german()

window.mainloop()
