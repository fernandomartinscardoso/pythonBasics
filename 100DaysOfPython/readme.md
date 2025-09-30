# 100 Days of Python Coding

Based on the course __100 Days of Code: The Complete Python Pro Bootcamp__ by Dr. Angela Yu, available at [Udemy Platform](https://www.udemy.com/course/100-days-of-code/).

## Day 1

How to use basic output (`print()`) and input commands, declare variables and concatenate strings. Final day project:

```python
print("Welcome to the Band Name Generator!")
user_city = input("What is the name of the city where you grew up in?\n")
user_pet = input("What is your pet's name?\n")
print("Your band name could be " + user_city + " " + user_pet)
```

## Day 2

How to convert variables using functions `float`, `int`, `str`, and `bool`:

- `float`: floating, real, decimal numbers, which can be rounded with `round(<var>, <ndigits>)`
- `int`: integer numbers
- `str`: strings, array of characters
- `bool`: boolean variables (`True` or `False`)

How to check the kind of variable using the function `type`.

How to use arithmetic operators:

| Operator       | Name           |
| :------------- | :------------- |
| +              | Addition       |
| -              | Subtraction    |
| *              | Multiplication |
| /              | Division       |
| //             | Floor division |
| %              | Modulus        |
| **             | Exponentiation |

The order of arithmetic operations in Python (PEMDAS).
PEMDAS is an acronym, which stands for:

1. Parentheses
1. Exponents
1. Multiplication/Division (from left to right)
1. Addition/Subtraction (from left to right)

Project of the day: [Tip Calculator](journey/day002.py).

## Day 3

How to control flow, and how to use comparison and logical operators. How to combine conditions (nested conditions with and without `elif`).

Comparison operators:

| Operator       | Name                     |
| :------------- | :----------------------- |
| ==             | Equal                    |
| !=             | Not equal                |
| >              | Greater than             |
| <              | Less than                |
| >=             | Greater than or equal to |
| <=             | Less than or equal to    |

Logical operators:

| Operator       | Name                                           |
| :------------- | :--------------------------------------------- |
| and            | Returns True if both statements are true       |
| or             | Returns True if one of the statements is true  |
| not            | Reverse the result                             |

Conditional Python structure:

```python
if condition1:
    process1
elif condition2:
    process2
    .
    .
    .
else:
    processn
```

How to interpret flow charts and turn them into Python code.

Project of the day: [Treasure Island Game](journey/day003.py).

## Day 4

How to use randomness in Python, since it is very important when building software, especially games. Computers use pseudorandom generators, e.g., [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister). Random module in Python docs are available [here](https://docs.python.org/3/library/random.html).

How to manipulate lists using indices (positive and negative), how to modify items, and how to add items using the function `append()`. Lists documentation is available [here]( https://docs.python.org/3/tutorial/datastructures.html).

The enumeration of a list starts at 0 for the first element. To count from last to first element, you must use negative indices, starting at -1 for the last element. The lists can be inserted into other lists, commonly called _nested list_, which is the base to create matrices in Python.

Project of the day: [Rock, Paper, Scissors Game](journey/day004.py).
