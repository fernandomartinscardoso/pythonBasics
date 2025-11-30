# 100 Days of Python
# Day 23 - Building a Complete Game
# Project of the day: The Turtle Crossing Game
# Player module

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)