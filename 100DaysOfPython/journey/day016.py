# 100 Days of Python
# Day 16 - Introduction to Object Oriented Programming (OOP)
# Project of the day: The Coffee Machine with OOP

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

while machine_is_on:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    coins = MoneyMachine()
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        machine_is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        coins.report()
    elif menu.find_drink(user_choice) is None:
        print("Sorry that item is not available.")
    else:
        price = menu.find_drink(user_choice).cost
        ingr = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(ingr):
            if coins.make_payment(price):
                 coffee_maker.make_coffee(ingr)
