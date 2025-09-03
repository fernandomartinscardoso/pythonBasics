# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 3.3
# Student: Fernando Cardoso
# Date: 02.08.2025
# Tasks:
# Write rules for the colors of the graphic elements in your project. 
# You can use “random” draws, you can make the color vary with the position of the element, 
# or even link the color to the type of element that is drawn.

import py5
from random import randint

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(693, 980)
    py5.background(0, 0, 200)

    cols = 4
    rows = 6
    offset_x = 50 # Margin from the left and right edges
    w = (py5.width - 2*offset_x) / cols
    offset_y = (py5.height - w*rows)/2 # Centering margin from top and bottom edges
    for j in range(rows):
        y = j * w + w/2 + offset_y
        for i in range(cols):
            x = i * w + w/2 + offset_x
            if j % 2 == 0:
                concentric_circles(x, y, 4, w-5)
            else:
                concentric_circles(x, y, 4, w-5)

def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.stroke(0)
    for i in range(n):
        py5.fill(randint(0, 255), randint(0, 255), randint(0,255))
        py5.circle(x, y, d - i * d/n)


py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_3_3.png') # Save a snapshot of the sketch window as a PNG file.
