# 100 Days of Python
# Day 22 - Building a Complete Game
# Project of the day: The Famous Arcade Game Pong

# Expected elements:
# - Paddle class to create paddles for both players
# - Ball class to create the ball and handle its movement
# - Scoreboard class to keep track of the score

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

screen.listen()
screen.onkey()


screen.exitonclick()
