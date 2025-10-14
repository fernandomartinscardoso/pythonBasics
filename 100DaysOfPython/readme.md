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

## Day 5

How to use loops in Python.

__Syntax of `for`__

```python
for <item_var> in <list_of_items>:
    process1
    process2
    ...
```

How to use the function `range`, that creates an interval of integers when combined with another function, like the loop `for`.
Example:

```python
for number in range(1, 10):
    print(number)
```

This code will print the numbers from 1 to 9, one number per row. The range of numbers can be expressed as $$a \leq range(a, b) < b$$ where the range of numbers is inclusive of the lower bound, but not inclusive of the upper bound.

Project of the day: [The Password Generator](journey/day005.py).

## Day 6

How to use __built-in functions__: Python interpreter has a number of functions and types built into it that are always available. [They are listed here in alphabetical order.](https://docs.python.org/3/library/functions.html)

How to define a new function, as per structure:

```python
def <function name>():
    print("Hello")
    process1
    process2
    ...
```

To call the function, just type it as the command `<function_name>()`. Example:

```python
#Creating the function
def user_name():
    # Inside the function
    name = input("What is your name? ")
    print("Hello, " + name)
    
#Outside the function
user_name() # Calling the function
```

Project to test the usage of functions in Python: [Reeborg's World](https://reeborg.ca/index_en.html).

How to use identation. Check for [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/).

How to create loops using `while`. Structure of syntax:

```python
while <condition_is_true>:
    process1
    process2
    ...
```

If the condition does not achieve a `False` state, the program will run on an _infinite loop_. We must be careful to avoid this condition.

Answer to [Hurdle 3](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json) challenge of Reeborg's World:

```python
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:   # or while not at_goal():
    if wall_in_front() == True:
        one_hurdle()
    elif front_is_clear()== True:
        move()
```

Answer to [Hurdle 4](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json) challenge of Reeborg's World:

```python
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_hurdle():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_in_front() == False:
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front() == True:
        one_hurdle()
    else:
        move()
```

Project of the day: [The Reeborg's Maze](journey/day006.py). Test files are available [here](originalCourseFiles/Reeborg+World+Tests.zip), which can be loaded from menu `Additional options -> Open world from file`.

## Day 7

Review of previous days. Project of the day: [The Hangman Game](journey/day007.py).

## Day 8

How to set functions with inputs. Structure:

```python
def my_function(<parameter>):
    process using <parameter>
    ...

# To call the function:
my_function(<value_of_parameter>)
```

To set a function with multiple inputs, the parameter must be separated by comma: `my_function(<parameter1>, <parameter2>, <parameter3>)`.

The parameters must be set in the same order they are defined by the function, since Python functions follow the logic of _positional parameters_.

If the parameter name is called together with its value (_keyword arguments_), then the order can be changed: `my_function(parameter2 = <value1>, parameter3 = <value2>, parameter1 = <value3>)`.

How to use `index`. The `index()` method returns the position at the first occurrence of the specified value. Syntax: `list.index(element, start, end)`. The `element` to search for is the only required parameter.

Project of the day: [The Caesar Cipher](journey/day008.py). Reference for the project: [Cryptography, History and Usage of the Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

## Day 9

How to implement dictionaries. A dictionary in Python is a data structure that allows us to associate a key to a value and pair the two pieces of data together. Example:

```python
# Colour of fruits
fruit_colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}
```

To retrieve items from a dictionary, just use the key as index value, e.g., `fruit_colours[banana]` returns `yellow` as value.

To add an item to the dictionary, you can use the new key as new index and attribute the value for this entry, e.g., `fruit_colours["peach"] = "pink"`. If the key already exists, this command will edit the data associated to it.

Dictionaries in Python accept nested lists and even other dictionaries:

```python
my_dictionary = {
    key1: [my_list],
    key2: {other_dictionary},
}
```

To access information in nested lists, a secondary index must be used for the inner list, e.g., given the list `nested_list = ["A", "B", ["C", "D"]]`, the command `nested_list[2][1]` access the element `"D"`.

Project of the day: [The Secret Auction Program](journey/day009.py).

## Day 10

How to use functions with outputs. The full syntax of the function contains the inputs, the body (where logic is defined) and return of output, like this:

```python
def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
```

How to convert strings to Title Case in Python. Just use the function `title()` associated to the string, for example, `"HeLLo".title()` returns `"Hello"`, `"new york".title()` returns `"New York"`, and so on.

__Return vs. print__ methods as function output: The `return` statement is used to give back a value from a function, which can be used later, while `print` is used to display a value to the console only for the programmer to see. Classic example:

```python
# The Leap Year Checker
def is_leap_year(year):
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        return True
    else:
        return False

print(is_leap_year(<year_to_check>))
```

How to use _docstrings_ to write multiline comments that document your code. Just enclose your text inside a pair of three double quotes. Example:

```python
"""
Torches are made to light, jewels to wear,
Dainties to taste, fresh beauty for the use,
Herbs for their smell, and sappy plants to bear;
Things growing to themselves are growth's abuse,
Seeds spring from seeds, and beauty breedeth beauty;
Thou wast begot; to get it is thy duty.

 William Shakespeare
 """
```

Project of the day: [The Calculator](journey/day010.py).
