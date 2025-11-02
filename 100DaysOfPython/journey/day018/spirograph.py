# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Task of the day: Drawing with Turtle

from turtle import Turtle, Screen
from random import randint, choice

print("Spirograph Turtle")
user_number_of_circles = int(input("How many circles do you want to draw?\n"))

screen = Screen()
screen.colormode(255)

# RGB colormap
def rgb_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "blue")
timmy.pensize(1)
timmy.speed("fastest")

def spirograph(number_of_circles):
    angle = 360 / number_of_circles
    for i in range(number_of_circles):
        timmy.pencolor(rgb_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + angle)

spirograph(user_number_of_circles)

screen.exitonclick()
