# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 9 of the course.
# Theme: Randomness and infinite loops part 2

import py5
from random import randint, choice

def setup():
    py5.size(980, 980)
    py5.fill(0)
    py5.no_stroke()
    py5.rect_mode(py5.CENTER) # Center rectangles by their center point

    for x in range(50, 930, 100):
        v = randint(1, 5)
        if v == 1:
            py5.circle(x, 450, 50)
        elif v == 2:
            py5.square(x, 450, 50)
        else:
            r = choice((10, 25, 40))
            star(x, 450, r, 30, v)

def star(cx, cy, ra, rb, np, angle=0):
    step = py5.TWO_PI / np
    py5.begin_shape()
    for i in range(np):
        a = angle + i * step + py5.frame_count/50
        ax = cx + py5.cos(a) * ra
        ay = cy + py5.sin(a) * ra
        py5.vertex(ax, ay)
        bx = cx + py5.cos(a + step/2) * rb
        by = cy + py5.sin(a + step/2) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)

py5.run_sketch() # Run the sketch to see the setup and draws applied.