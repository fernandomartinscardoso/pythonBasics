# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Task of the day: Drawing with Turtle

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "green")

# RGB colormap
def rgb_color():
    global red, green, blue
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
for j in range(3,11):
    angle = 360/j
    rgb_color()
    for i in range(j):
        timmy.pencolor(red, green, blue)
        timmy.right(angle)
        timmy.forward(100)

screen.exitonclick()