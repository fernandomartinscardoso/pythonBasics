# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Videos 8 and 9 of the course.
# Theme: Randomness and infinite loops part 1

import py5
from random import randint, choice, uniform

def setup():
    py5.size(980, 980)

    py5.fill(0)
    py5.no_stroke()

    # Repeat loops to draw circles with random diameters and colors
    for x in range(50, 930, 50):
        d = uniform(0, 50)
        py5.circle(x, 50, d)
    
    for y in range(50, 930, 50):
        i = randint(1, 4)
        py5.circle(y, 150, 10*i)

    for z in range(50, 930, 50):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        py5.fill(r, g, b)
        py5.circle(z, 250, 45)  

    for z in range(50, 930, 50):
        r = 0
        g = randint(0, 255)
        b = randint(0, 255)
        py5.fill(r, g, b)
        py5.circle(z, 350, 45) 

    for z in range(50, 930, 50):
        r = 0
        g = randint(128, 255)
        b = 128
        py5.fill(r, g, b)
        py5.circle(z, 450, 45)
    
    colors = [py5.color(255, 200, 0), 
              py5.color(0, 128, 255), 
              py5.color(128, 255, 0)]
    
    for z in range(50, 930, 50):
        py5.fill(choice(colors))
        py5.circle(z, 550, 45)

    py5.fill(0)
    for x in range(50, 930, 100):
        n = randint(3, 7)
        r = choice((10, 25, 40))
        star(x, 700, r, 50, n)

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