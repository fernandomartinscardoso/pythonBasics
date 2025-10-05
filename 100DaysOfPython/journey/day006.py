# 100 Days of Python
# Day 6 - Functions and while loops
# Project of the day: Reeborg's Maze
# Answer to the Reeborg's Maze challenge on https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if wall_on_right() == False:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()