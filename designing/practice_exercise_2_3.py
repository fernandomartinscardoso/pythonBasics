# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 2.3
# Student: Fernando Cardoso
# Date: 31.08.2025
# Tasks:
# Adapt one of the examples from the class "Randomness: infinite options", that is, use a repeat loop to draw a sequence of graphic elements with some type of random variation.

Use the element you created in the "Define and use a new function" task.

import py5
from random import randint

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(128, 200, 0)
    for i in range(1, 200):
        j = randint(1, 100)
        concentric_circles(98 + i*4, 98 + j*8, 10, 500/j)

def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.no_fill()
    py5.stroke(0)
    for i in range(n):
        py5.circle(x, y, d - i * d/n)


py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_2_3.png') # Save a snapshot of the sketch window as a PNG file.
