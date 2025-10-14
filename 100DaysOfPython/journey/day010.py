# 100 Days of Python
# Day 10 - Functions with Outputs
# Project of the day: The Calculator

import calc_art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def my_operation(number1, number2, operation):
    return calc_dict[operation](number1, number2)

print(calc_art.logo)

continue_operations = True

while continue_operations:
    num1 = float(input("Type the first number:\n"))
    oper = input("Type the operation: +, -, * or / \n")
    num2 = float(input("Type the second number:\n"))
    result = my_operation(num1, num2, oper)
    print(f"{num1} {oper} {num2} = {result}")
    loop_operation = input("Would you like to calculate other operation? yes or no\n")
    if loop_operation == "yes":
        print("Let's go do some more calculations!")
    elif loop_operation == "no":
        print("See you next time!")
        continue_operations = False
    else:
        print("Invalid option! \nGoodbye!")
        break
