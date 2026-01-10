# 100 Days of Python
# Day 29 - GUI with Tkinter - Saving Data and Creating Pop-ups
# Project of the day: Password Manager

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as f:
        f.write(website + " | ")
        f.write(email_user + " | ")
        f.write(password + "\n")
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

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
