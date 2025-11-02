# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Task of the day: Drawing with Turtle

from turtle import Turtle, Screen
from random import randint, choice

print("The Random Walk Turtle")
walks = int(input("Enter the number of walks: "))
steps = int(input("Enter the number of steps per walk: "))

screen = Screen()
screen.colormode(255)

# RGB colormap
def rgb_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color

directions = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "blue")
timmy.pensize(5)
timmy.speed("normal")

def random_walk(number_walks, number_steps):
    for i in range(number_walks):
        timmy.pencolor(rgb_color())
        for j in range(number_steps):
            timmy.right(choice(directions))
            timmy.forward(10)

random_walk(walks, steps)

screen.exitonclick()
