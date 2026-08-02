# 100 Days of Python
# Day 32 - Email and Dates Automation
# The Email Sender

import smtplib

my_email = "sender@gmail.com"
my_password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="receiver@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
