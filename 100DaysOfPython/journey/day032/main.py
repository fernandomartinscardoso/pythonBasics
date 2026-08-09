# 100 Days of Python
# Day 32 - Email and Dates Automation
# The Email Sender

import smtplib
import datetime as dt
import random

def choose_random_quote():
    global random_quote
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    return random_quote

def send_email():
    my_email = "sender@gmail.com"
    my_password = "app_password_here"

    with smtplib.SMTP("smtp.gmail.com") as connection: # Change the SMTP server if using a different email provider
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receiver@gmail.com",
            msg=f"Subject:'Motivational Sunday'\n\n{random_quote}."
    )


day_of_week = dt.datetime.now().weekday()
if day_of_week == 6:
    choose_random_quote()
    send_email()
