# 100 Days of Python
# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Project of the day: The Hirst Painting Project

from turtle import Turtle, Screen
from random import choice

# Final color list from color_import
colors_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
initial_x = -325
initial_y = -325

screen = Screen()
screen.colormode(255)
screen.screensize(670, 670, bg="lightgray")

t = Turtle()
t.penup()
t.hideturtle()
t.setposition((initial_x, initial_y))

for i in range(10):
    initial_y += 50
    t.setposition((initial_x, initial_y))
    for j in range(10):
        t.dot(20, choice(colors_list))
        t.forward(50)

screen.exitonclick()