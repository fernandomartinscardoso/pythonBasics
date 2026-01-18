# 100 Days of Python
# Day 19 - Turtle Graphics, Instance Attributes and States
# Project 2 of the day: Turtle Race

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def create_turtle(turtle_color, pos_x, pos_y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color)
    new_turtle.goto(x=pos_x, y=pos_y)
    turtles.append(new_turtle)

for i in range(6):
    create_turtle(colors[i], -230, -120+50*i)

if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:
    for turtle in turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        

screen.exitonclick()
