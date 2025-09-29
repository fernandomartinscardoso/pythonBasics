# 100 Days of Python
# Day 2 - Data Types in Python
# Project of the day: Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_per_person = (bill * (1 + tip/100))/people
bill_per_person_round = round(bill_per_person,2)

print(f"Each person should pay: ${bill_per_person_round}")
