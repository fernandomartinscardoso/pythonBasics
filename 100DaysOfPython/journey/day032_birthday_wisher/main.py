# 100 Days of Python
# Day 32 - Email and Dates Automation
# Project: Birthday Wisher

import smtplib
import datetime as dt
import pandas as pd
import random

# Creating today's date tuple
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

# Creating a dictionary from birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

# Creating a function to send email
def send_email(receiver_email, receiver_msg):
    my_email = "<your_email>@gmail.com"   # Replace with your email address
    my_password = "<your_app_password>"   # Replace with your app password (not your regular email password)

    with smtplib.SMTP("smtp.gmail.com") as connection: # Change the SMTP server if using a different email provider
        connection.starttls() # start TLS encryption for security
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{receiver_email}",
            msg=f"Subject:'Happy Birthday!'\n\n{receiver_msg}."
    )

# Checking if today matches a birthday in the birthdays.csv and sending email if it does
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    email = birthday_person["email"]
    random_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt", "r") as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[NAME]", name)
        send_email(email, letter_content)
