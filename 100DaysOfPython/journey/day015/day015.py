# 100 Days of Python
# Day 15 - Local Development Environment Setup 
# Project of the day: The Coffee Machine

from menu_and_resources import MENU, resources

print("Welcome to the Coffee Machine ☕")

water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
def resources_left():
    global water_left, milk_left, coffee_left
    water_left = resources["water"] - water
    resources["water"] = water_left
    milk_left = resources["milk"] - milk
    resources["milk"] = milk_left
    coffee_left = resources["coffee"] - coffee
    resources["coffee"] = coffee_left

water = 0
milk = 0
coffee = 0
money = 0
price = 0
change = 0
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

def check_transaction():
    global money, change
    user_order(user_choice)
    if sufficient_resources():
        total_inserted = process_coins()
        if total_inserted >= price:
            money += price
            change = total_inserted - price
            resources_left()
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            else:
                print("You inserted the correct value for your drink.")
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Call maintenance team.")


machine_is_on = True

while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_is_on = False
    elif user_choice == "report":
        print(f"Water: {water_left}ml\n"
              f"Milk: {milk_left}ml\n"
              f"Coffee: {coffee_left}g\n"
              f"Money: ${money:.2f}")
    elif user_choice == "espresso":
        check_transaction()
    elif user_choice == "latte":
        check_transaction()
    elif user_choice == "cappuccino":
        check_transaction()
    else:
        print("Invalid option! Try again! 🐸")
