# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 3, Video 4 of the course.
# Theme: Quickly generating poster variations

import py5
from random import randint, seed, uniform as random

s = 1 # Seed for random number generator

def setup():
    py5.size(700, 980)

def draw():
    seed(s)
    py5.background(0, 0, 100)
    # py5.no_stroke()
    for i in range(3):
        grid(6, 8, 100)

def grid(cols, rows, offset_x):
    py5.stroke(255)
    # cols is number of columns
    # rows is number of rows
    # offset_x is the margin from the left and right edges
    w = (py5.width - 2*offset_x) / cols
    offset_y = (py5.height - w*rows)/2 # Centering margin from top and bottom edges
    for j in range(rows):
        y = j * w + w/2 + offset_y
        r = randint(0, 128)
        g = randint(128, 255)
        b = randint(0, 255)
        py5.fill(r, g, b)
        for i in range(cols):
            x = i * w + w/2 + offset_x
            m = randint(1, 6)
            if m == 1:
                py5.fill(r, g, b, 128)
                ra = random(w/20, w/2)
                rb = random(1, w/2)
                np = randint(4, 10)
                star(x, y, ra, rb, np)
            elif 1 < m < 4:
                py5.fill(255, 64)
                dr = randint(0, 1)*w/2
                py5.rect(x-dr, y-dr, w/2, w/2)
            elif 4 <= m < 6:
                py5.fill(200, 64)
                py5.rect(x-w/2, y-w/2, w, w)
            else:
                py5.fill(r, g, b, 64)
                py5.circle(x, y, randint(1,2)*w/4)

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

def mouse_pressed():
    global s
    s += 1
    print(s)
    py5.redraw() # Redraw the canvas on mouse press

def key_pressed():
    if py5.key == 's':
        py5.save_frame(f'drawing_u3_v4_seed_{s}.png')

py5.run_sketch() # Run the sketch to see the setup and draws applied.