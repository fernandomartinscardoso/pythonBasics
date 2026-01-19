# 100 Days of Python
# Day 30 - Errors, Exceptions and JSON Data
# Project of the day: Password Manager

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for char in range(nr_letters)]

    password_list += [choice(symbols) for char2 in range(nr_symbols)]

    password_list += [choice(numbers) for char3 in range(nr_numbers)]

    shuffle(password_list) # Shuffle the characters in the password list

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password) # Copying password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(email_user) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty! 😅")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Cleaning entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

# Canvas setup
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

email_user_label = Label(text="Email/Username:", bg="white")
email_user_label.grid(column=0, row=2)

# Entries
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_user_entry = Entry(width=43)
email_user_entry.insert(0, "fernando@email.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password", command=gen_pass)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_pass, width=40)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
