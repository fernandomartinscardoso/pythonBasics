# 100 Days of Python
# Day 23 - Building a Complete Game
# Project of the day: The Turtle Crossing Game

import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    car_manager.create_car()
    car_manager.move_car()

    # Collision with cars:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Successful crossing:
    if player.ycor() == FINISH_LINE_Y:
        player.reset_position()
        car_manager.level_up()
        scoreboard.level()

screen.exitonclick()