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

## Day 11

Review of concepts: list manipulation, usage of the function `sum()`, usage of library `math`, and algorithm development.

Summary of Python list methods:

| Method | Description | Example | Returns/Effect |
| :--- | :--- | :--- | :--- |
| __`append(element)`__ | Adds a single `element` to the end of the list. | `L.append(4)` | Modifies the list in-place. |
| __`insert(index, element)`__ | Inserts an `element` at the specified `index`. | `L.insert(1, 'a')` | Modifies the list in-place. |
| __`extend(iterable)`__ | Adds all elements of an `iterable` (like another list) to the end of the list. | `L.extend([5, 6])` | Modifies the list in-place. |
| __`remove(element)`__ | Removes the __first__ occurrence of the specified `element`. Raises a `ValueError` if the element is not found. | `L.remove(2)` | Modifies the list in-place. |
| __`pop([index])`__ | Removes and returns the element at the specified `index`. If no index is given, it removes and returns the __last__ element. | `L.pop(0)` or `L.pop()` | Returns the removed element. Modifies the list in-place. |
| __`clear()`__ | Removes all items from the list, making it empty. | `L.clear()` | Modifies the list in-place. |
| __`index(element, [start], [end])`__ | Returns the __index__ of the first occurrence of the `element`. Raises a `ValueError` if the element is not found. | `L.index(3)` | Returns an integer (the index). |
| __`count(element)`__ | Returns the number of times the specified `element` appears in the list. | `L.count(2)` | Returns an integer (the count). |
| __`sort(key=None, reverse=False)`__ | Sorts the list __in-place__. Arguments `key` and `reverse` are optional. | `L.sort()` or `L.sort(reverse=True)` | Modifies the list in-place. Returns `None`. |
| __`reverse()`__ | Reverses the elements of the list __in-place__. | `L.reverse()` | Modifies the list in-place. |
| __`copy()`__ | Returns a __shallow copy__ of the list. | `L2 = L.copy()` | Returns a new list. |

Project of the day: [The Blackjack Capstone](journey/day011.py).

## Day 12

How to use local and global scopes. Variables (or functions) declared inside functions have _local scope_ (also called _function scope_). They are only seen by other code within the same block of code. Example:

```python
def my_function():
    local_var = 2
    
# This will cause a NameErrorr because local_var is only defined inside the function
print(local_var)
```

Variables or functions declared at the top level (unindented) of a code file have _global scope_. It is accessible anywhere in the code file. Example:

```python
global_var = 3

def my_function():
    # This works without any problems
    print(global_var)
```

Python, differently from other languages, does not have _block scopes_. This means that variables created nested in other blocks of code, e.g., for loops, if statements, while loops, etc., don't get local scope. They are given _function scope_ if they are within a function or _global scope_ if they are not. Example:

```python
# Accessible anywhere
global_var = 1

def my_function():
    # Only accessible within my_function()
    local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    block_var = 3
```

The code can be forced to allow you to modify something with global if you use the `global` keyword before you use it. Example:

- This will give you an error:

```python
a = 1
def my_function():
    a += 1
    print(a)
```

- But this will work:

```python
a = 1
def my_function():
    global a
    a += 1
    print(a)
```

It is a good practice to use global variables to define constant values. It is not mandatory, but the most used name convention for constants is to declare them all caps and with underscore to separate the words. Example:

```python
PI = 3.14159
GOOGLE_URL = "https://www.google.com" 
```

Project of the day: [The Number Guessing Game](journey/day012.py).

## Day13

How to debug in Python. Some bugs only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug. Example:

```python
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
```

In the code above, the dice face `❶` is never reachable because the list positions start at 0, and when `dice_num` is equal to 6, the position is out of range, since last position is 5.

### Debug strategies

- __Play Computer Method__

    Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

- __Catching Exceptions__

    You can use a __try/except__ block in Python to catch any exceptions that might occur. For example, if you imagine there could be a chance of user error. You can prevent it crashing your code by anticipating it. You trap the dangerous code inside a try block and use an except block to catch any potential errors. Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.
    The structure has two main parts:
    1. `try` block: Contains the code that might potentially raise an exception (error).
    2. `except` block: Contains the code that executes if an exception is raised in the `try` block.
    Example:

    ```python
    try:
        # 1. Code that might fail
        result = 10 / 0 
    except:
        # 2. Code that executes if an error occurs
        print("An error occurred! Cannot divide by zero.")
        result = 0 # Provide a safe default value

    print(f"The final result is: {result}")
    # Output:
    # An error occurred! Cannot divide by zero.
    # The final result is: 0
    ```

- __Use `print()`__

    It can help expose hidden values while your code is running. The `print` function can be used to expose intermediate values hidden by internal processes like repetition loops, and help you debug your code.

- __Use a debugger__

    Most IDEs (Integrated Development Environments) such as PyCharm and VSCode will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.
    Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.
    Debugger main tools in PyCharm:
    1. __Breakpoint__ - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.
    1. __Step Over__ - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.
    1. __Step Into__ - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.
    1. __Step Into My Code__ - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

- __External support__

    Check for the problems with experts or on Internet, as in [StackOverflow](https://stackoverflow.com/questions/tagged/python).

## Day 14

How to create a game that compares the number of followers between two social media profiles. The comparison continues while the player is right guessing the answer, and finishes when the guess is wrong, providing the score to the player. The project is based on the classic online game [Higher or Lower](https://www.higherlowergame.com/).

Project of the day: [Higher or Lower Game](journey/day014.py).

## Day 15

How to use [Pycharm keyboard shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html?keymap=secondary_windows).

Source for emojis to be used in the output to improve interface design: [Emojipedia](https://emojipedia.org/hot-beverage).

How to code a coffee vending machine according to the [requirements](journey/day015_requirements.py).

Project of the day: [The Coffee Machine Project ☕](journey/day015.py).

## Day 16

### Introduction to Object-Oriented Programming (OOP)

Until now, all codes developed were based on __Procedural Programming__, which is a programming paradigm that revolves around the concept of a _procedure call_.

__Procedures__ (also known as routines, subroutines, methods, or functions) contain a series of computational steps to be carried out. The program is typically structured as a sequence of instructions, usually grouped into these procedures, that tell the computer how to perform a task. It emphasizes breaking down a large program into smaller, manageable parts (the procedures) and focuses on the logic and order of execution.

Since procedural programming was one of the oldest method to approach sofware developement, it is commonly associated with languages like __C__, __Pascal__, and __Fortran__. Due to its simplicity and structure, it has the advantages of being easy to follow and implement, providing reusable code, modular design and efficiency, especially when the project is small and of low complexity. However, procedural programming has limitations, particularly when dealing with complex, large-scale applications, difficulting the management and evolution of the project.

__Object-Oriented Programming (OOP)__ is a programming paradigm that organizes software design around __objects__ rather than procedures and logic. An object is a software entity that encapsulates both data (attributes or state) and the functions (methods or behavior) that operate on that data.

The core idea is to model real-world entities as self-contained objects that interact with each other. This contrasts with procedural programming, which focuses on a sequence of steps.

#### Key Concepts of OOP

1. __Classes and Objects__:
    - A __Class__ is a blueprint or template for creating objects, defining what properties and methods all objects of that type will have.
    - An __Object__ is a concrete _instance_ of a class, with its own specific data values.
2. __Encapsulation__: This is the bundling of data and the methods that operate on that data within a single unit (the object). Crucially, it also involves data hiding, where the object's internal state is protected and can only be modified through the object's own public methods, creating a barrier against accidental corruption.
3. __Inheritance__: This mechanism allows a new class (subclass or child class) to take on the properties and methods of an existing class (superclass or parent class). This promotes __code reusability__ and establishes a clear __"is-a"__ relationship between classes (__"[Subclass] is a [Superclass]"__). Example: If you have a __class__ named `Car` and another __class__ named `Sedan`, the relationship is: __"A Sedan is a Car."__
4. __Polymorphism__: Meaning "many forms", this allows objects of different classes to be treated as objects of a common type. For example, a general `makeSound()` method can execute different behaviors (roaring, chirping, barking) depending on whether the object calling it is a `Lion`, a `Bird`, or a `Dog`.
5. __Abstraction__: This involves showing only essential information to the user while hiding the complex implementation details. It focuses on _what_ an object does rather than _how_ it does it, simplifying the system interface.

### OOP in Python

A class in Python is generally writing with __PascalCase__, which is a programming naming convention where compound words are joined without spaces, and the first letter of every word is capitalized. The object is an instance of the class, e.g., for an object named `car` that is an instance of the class `CarBlueprint`, the structure would be:

```python
car = CarBlueprint()
```

The object has its __attributes__, and they can be accessed using a dot between the object and the attribute name, e.g., if the `car` has the `speed` and `fuel` as attributes, you can access the `speed` using the syntax `car.speed`.

The object also has its __methods__, and they are functions defined inside a class that define the behaviors of objects created from that class. While the __attributes__ specify what the object _has_, the __methods__ specify of the object _does_. For example, that same object called `car` mentioned before could have a method to break named `stop`, and it could be called as:

```python
car.stop()
```

Taking the example from Dr. Yu's class, it's possible to identify the elements of OOP in Python:

```python
from turtle import Turtle, Screen

tommy = Turtle()
print(tommy)
tommy.shape("turtle")
tommy.color("red", "green")
tommy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```

The code above uses [Turtle Graphics](https://docs.python.org/3/library/turtle.html) library to create a screen with a turtle drawn in [green and red](https://cs111.wellesley.edu/reference/colors) that moves 100 steps forward. The OOP elements are:

- Object: `tommy`
- Classes: `Turtle()` and `Screen()`
- Attribute: `canvheight`
- Methods: `shape()`, `color()`, `forward()`, and `exitonclick()`

The next example requires a package to print formatted tables, and the best place to find packages like that is in the [PyPI portal](https://pypi.org/), that is a repository of software for the Python programming language. For the tables requested, the package [PrettyTable](https://pypi.org/project/prettytable/) is a good option.
Example: Print the table below in the terminal:

| Pokemon Name | Type    |
| :----------- | :---    |
| Pykachu      | Electric|
| Squirtle     | Water   |
| Charmander   | Fire    |

Code:

```python
from prettytable import PrettyTable

table = PrettyTable()

# Method with rows:
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

# Method with columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
```

Output:

```terminal
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
```

__Curiosity__: [Steve Jobs interview](https://www.rollingstone.com/culture/culture-news/steve-jobs-in-1994-the-rolling-stone-interview-231132/) to Rolling Stones magazine on OOP.

Project of the day: [The Coffee Machine Project with OOP ☕](journey/day016.py).

## Day 17

How to use the different letter cases to distinguish classes, attributes and methods:

- __PascalCase__: all words are typed together, but the first letter of each word is upper case;
- __camelCase__: similar to PascalCase, but the first letter of the first word is lower case;
- __snake_case__: all letters are lower case, but the words are connected by underscore.

The PascalCase is commonly used for class names, and snake_case for everything else. I personally like to use camelCase to name directories and repositories.

### Detailing OOP with Python

__Attributes__ are _variables_ associated to an _object_ in the form: `object.attribute`.

__Constructor__ part of the BluePrint that specifies what should happen when our object is being constructed, which is known in programming as _initializing an object_. In Python, there is a special function to initialise the object and create the constructor named `__init__`, that follows the structure:

```python
class ClassName:
    def __init__(self):
        # initialise attributes
```

Inside the function `__init__`, we the attributes, or define the initial values of the attributes.

The `__init__` function is going to be called everytime a new `object` from its `class` is created. The parameter `self` refers to the object itself. After `self` the other attributes must be added, if they are necessary, for example:

```python
class Car:
    def __init__(self, seats):
        self.seats = seats
```

Project of the day: [The Quiz Game](journey/quizGame).

To improve the database, it was used the data available at [Open Trivia Database](https://opentdb.com/).

## Day 18

How to use more resources of the Turtle Graphics library. How to use __tuples__ and import modules.

References for Turtle:

- [Turtle documentation](https://docs.python.org/3/library/turtle.html)
- [Reference of colors on trinket](https://trinket.io/docs/colors)
- [Turtle colors on cs111](https://cs111.wellesley.edu/reference/colors)

### Importing modules

- The whole library:

```python
import random

var = random.randint(0, 100)
```

- One function:

```python
from random import randint

var = randint(0, 100)
```

- All functions:

```python
from random import *

var1 = randint(0, 100)
var2 = choice([0, 1, 2, 3])
```

- Changing library's name:

```python
import random as rand

var = rand.randint(0, 100)
```

Exercises on how to make the `turtle` move on the screen following classic algorithms like the [Random Walk](https://en.wikipedia.org/wiki/Random_walk).

### Tuples and Lists

Lists and Tuples are two of the most commonly used sequence data types in Python, but they differ fundamentally in their mutability and use cases. Mutability is the most important difference:

- __List__: If you have a list `my_list = [10, 20]`, you can later add `30` to it (`my_list.append(30)`).
- __Tuple__: If you have a tuple `my_tuple = (10, 20)`, attempting to add an element will result in an error, as its structure is fixed.

The tuples have less methods than lists, and the main ones are: `count()` (counts occurrences of an element) and `index()` (finds the first index of an element).

As you may noticed, the syntax of the lists is defined using square brackets `[]`, while tuples are defined using parentheses `()`.

### The Hirst Painting Project

How to use the package `colorgram` to extract colors from an image.

How to test the colors extracted using the [RGB Calculator](https://www.w3schools.com/colors/colors_rgb.asp).

Project of the day: [The Hirst Painting](journey/hirstPainting).

## Day 19

How to use Turtle Events Listeners. According to [Turtle Documentation](https://docs.python.org/3/library/turtle.html#turtle.listen), `turtle.listen()` set focus on TurtleScreen in order to collect key-events. Example:

```python
from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
```

The program above creates a turtle that moves 10 steps each time the `space` bar is pressed. Notice the usage of __functions as inputs__. Given two functions `function_a(something)` and `function_b()`, such as:

```python
def function_a(something):
    #Do this with something
    #Then do this
    #Finally do this

def function_b():
    #Do this
```

Since `function_a` admits parameter, `function_b` can be used as parameter of the `function_a` by removing the parenthesis:

```python
function_a(function_b)
```

A function that takes another function as input is called _higher order function_. In the example above, `function_a` is the higher order function.

### Instances and states

In OOP, _instance_ and _state_ are two distinct but closely related concepts that define an object.

1. __Instance (or Object)__: an instance (often used interchangeably with the term object) is a concrete realization of a class. Think of a class as a __blueprint__ or a __template__. It defines the structure (what data it holds) and the behavior (what actions it can perform). Example: A `Car` class defines that every car will have properties like `color`, `make`, and `speed`, and methods like `accelerate()` and `brake()`. Therefore, the instance is the actual thing created from that blueprint in the computer's memory. It is a __runtime entity__. Following the same example: `myCar` is an instance of the `Car` class. `yourCar` is another, separate instance of the `Car` class.
2. __State__: The state of an object is the __set of values__ currently held by its instance variables (or __attributes__) at any given moment. Example based on the `Car` class:

    | Instance Variable/Attribute | Value in Instance 1 (`myCar`) | Value in Instance 2 (`yourCar`) |
    | :-------------------------- | :---------------------------- | :------------------------------ |
    | `color`                     | "Red"                         | "Blue"                          |
    | `make`                      | "Honda"                       | "Ford"                          |
    | `speed`                     | 50                            | 0                               |

Projects of the day: [The Etch-A-Sketch App](journey/day019_proj_1.py) and [The Turtle Race Game](journey/day019_proj_2.py).
