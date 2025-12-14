# 100 Days of Python
# Day 25 - Introduction to Pandas
# Second Project of the day: US States Game

import turtle
import pandas

# Set up the screen with the US map
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

# Read the states data from the CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop: while the number of guessed states is less than 50 or until the user types "Exit"
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title().strip()
    # If the user types "Exit", create a CSV file with the states that were not guessed
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
