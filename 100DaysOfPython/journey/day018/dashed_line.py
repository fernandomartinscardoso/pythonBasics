# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Task of the day: Drawing with Turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "purple")

# Drawing a dashed line
for i in range(50):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
