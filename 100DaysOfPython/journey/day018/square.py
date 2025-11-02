# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Task of the day: Drawing with Turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "purple")

# Drawing a square
for i in range(4):
    timmy.right(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
