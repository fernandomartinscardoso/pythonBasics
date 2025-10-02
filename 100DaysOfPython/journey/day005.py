# 100 Days of Python
# Day 5 - Loops with for and range functions
# Project of the day: Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create a list to hold the characters of the password
password_list = []

for let in range(nr_letters):
    password_list.append(random.choice(letters))

for sym in range(nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list to ensure randomness
# Alternatively, the method random.shuffle(password_list) could be used to generate password_scrambled
total_char = nr_letters + nr_symbols + nr_numbers
password_scrambled = []

for char in range(total_char):
    b = len(password_list) - 1
    password_scrambled.append(password_list.pop(random.randint(0, b)))

# Join the characters to form the final password string
password = ''

for pass_char in password_scrambled:
    password += pass_char

print(f"Your strong password is {password}")
