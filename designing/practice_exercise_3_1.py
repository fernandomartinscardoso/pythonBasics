# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 3.1
# Student: Fernando Cardoso
# Date: 02.08.2025
# Tasks:
# Choose a graphic element of your choice and produce a grid repeating this element in rows and columns.

import py5
from random import randint

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(693, 980)
    py5.background(100, 0, 100)

    cols = 10
    rows = 15
    offset_x = 50 # Margin from the left and right edges
    w = (py5.width - 2*offset_x) / cols
    offset_y = (py5.height - w*rows)/2 # Centering margin from top and bottom edges
    for j in range(rows):
        y = j * w + w/2 + offset_y
        for i in range(cols):
            x = i * w + w/2 + offset_x
            concentric_circles(x, y, 3, w)

def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.fill(232, 216, 135) # Fill color for the circles
    py5.stroke(0)
    for i in range(n):
        py5.circle(x, y, d - i * d/n)


py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_3_1.png') # Save a snapshot of the sketch window as a PNG file.
