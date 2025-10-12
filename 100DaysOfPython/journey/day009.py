# 100 Days of Python
# Day 9 - Dictionaries and Nesting
# Project of the day: The Secret Auction Program

import bid_art

print(bid_art.logo)

entry = True
bid_dict = {}
while entry:
    name = input("Type the user name:\n")
    price = float(input("Enter the user bid:\n$"))
    bid_dict[name] = price
    new_user_yes_or_no = input("Insert new user? Type yes or no\n").lower()
    if new_user_yes_or_no == "no":
        entry = False
    elif new_user_yes_or_no == "yes":
        print("\n"*50) # Clear the console
        print("Please enter new user data.")
    else:
        print("Invalid option! \nOnly valid entries are going to be checked.")
        break

max_bid = 0
winner_name = ""
for name in bid_dict:
    if bid_dict[name] > max_bid:
        max_bid = bid_dict[name]
        winner_name = name

print(f"{winner_name} is the winner with the bid of ${max_bid}!")
