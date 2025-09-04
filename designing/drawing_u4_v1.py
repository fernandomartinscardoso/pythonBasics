# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 4, Video 1 of the course.
# Theme: Recursive grid

import py5
from random import randint, seed, uniform as random

save_document = False # Variable to control saving the document, based on drawing_u4_v2_0.py
s = 1 # Seed for random number generator

def setup():
    py5.size(700, 980)

def draw():
    global save_document
    if save_document:
        py5.begin_record(py5.PDF, f'output/poster_{s}.pdf')
    seed(s)
    py5.background(0, 0, 100)
    for _ in range(3):
        grid(4, 6, 50, 40, 600)
    if save_document:
        py5.end_record()
        save_document = False
        print('Document saved.')

def grid(cols, rows, offset_x, offset_y, wt):
    py5.stroke(255)
    # cols is number of columns
    # rows is number of rows
    # offset_x is the margin from the left and right edges
    w = wt / cols
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
                py5.stroke(0)
                ra = random(w/20, w/2)
                rb = random(1, w/2)
                np = randint(4, 10)
                star(x, y, ra, rb, np)
            elif 1 < m < 4:
                py5.fill(255, 34)
                py5.stroke(r, g, b)
                dr = randint(0, 1)*w/2
                py5.rect(x-dr, y-dr, w/2, w/2)
            elif 4 <= m < 6:
                py5.fill(200, 64)
                py5.stroke(r, g, b)
                py5.rect(x-w/2, y-w/2, w, w)
            else:
                py5.fill(r, g, b, 64)
                py5.stroke(0)
                py5.circle(x, y, randint(1,2)*w/4)
            if randint(1, 3) == 3 and w > 30:
                grid(2, 2, x-w/2, y-w/2, w)
            

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
    global save_document
    if py5.key == 's':
        py5.save_frame(f'drawing_u4_v1_seed_{s}.png')
    elif py5.key == 'p':
        save_document = True
        print('Saving document...')

py5.run_sketch() # Run the sketch to see the setup and draws applied.