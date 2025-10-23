# 100 Days of Python
# Day 15 - Local Development Environment Setup 
# Project of the day: The Coffee Machine

from menu_and_resources import MENU, resources

water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
def resources_left():
    global water_left, milk_left, coffee_left
    water_left = resources["water"] - water
    milk_left = resources["milk"] - milk
    coffee_left = resources["coffee"] - coffee

water = 0
milk = 0
coffee = 0
money = 0
price = 0
def user_order(user_input):
    global water, milk, coffee, price
    water = MENU[user_input]["ingredients"]["water"]
    milk = MENU[user_input]["ingredients"]["milk"]
    coffee = MENU[user_input]["ingredients"]["coffee"]
    price = MENU[user_input]["cost"]

def sufficient_resources():
    if water > water_left:
        print("Sorry, there is not enough water")
        return False
    elif milk > milk_left:
        print("Sorry, there is not enough milk")
        return False
    elif coffee > coffee_left:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True

quarters = 0
dimes = 0
nickles = 0
pennies = 0
def process_coins():
    global quarters, dimes, nickles, pennies
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes:"))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies:"))
    money_inserted = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return money_inserted

machine_is_on = True

while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_is_on = False
    elif user_choice == "report":
        print(f"Water: {water_left}ml\n"
              f"Milk: {milk_left}ml\n"
              f"Coffee: {coffee_left}g\n"
              f"Money: ${money}")
    elif user_choice == "espresso":
        user_order(user_choice)
        sufficient_resources()
        if sufficient_resources():
            pass
    elif user_choice == "latte":
        user_order(user_choice)
        sufficient_resources()
        if sufficient_resources():
            pass
    elif user_choice == "cappuccino":
        user_order(user_choice)
        sufficient_resources()
        if sufficient_resources():
            pass
    else:
        print("Invalid option! Try again! 🐸")