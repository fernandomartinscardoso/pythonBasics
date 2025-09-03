# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 3.4
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
    py5.background(128)

    cols = 10
    rows = 15
    offset_x = 50 # Margin from the left and right edges
    w = (py5.width - 2*offset_x) / cols
    offset_y = (py5.height - w*rows)/2 # Centering margin from top and bottom edges
    for j in range(rows):
        y = j * w + w/2 + offset_y
        for i in range(cols):
            x = i * w + w/2 + offset_x
            s = randint(0, 6)
            if s <= 2:
                concentric_circles(x, y, randint(1,4), w-5*randint(0,5))
            elif 2 < s <= 5:
                py5.fill(randint(0, 200), 150)
                dr = randint(0, 1)*w/2
                py5.rect(x-dr, y-dr, w, w)
            else:
                py5.fill(randint(0, 200), 150)
                ra = randint(5, int(w/2))
                rb = randint(5, int(w/2))
                np = randint(4, 10)
                star(x, y, ra, rb, np)
def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.stroke(0)
    for i in range(n):
        py5.fill(randint(0, 255))
        py5.circle(x, y, d - i * d/n)

def star(cx, cy, ra, rb, np, angle=0):
    step = py5.TWO_PI / np
    py5.begin_shape()
    for i in range(np):
        a = angle + i * step
        ax = cx + py5.cos(a) * ra
        ay = cy + py5.sin(a) * ra
        py5.vertex(ax, ay)
        bx = cx + py5.cos(a + step/2) * rb
        by = cy + py5.sin(a + step/2) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)

py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_3_4.png') # Save a snapshot of the sketch window as a PNG file.
