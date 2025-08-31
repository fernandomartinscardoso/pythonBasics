# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 3, Video 2 of the course.
# Theme: A grid of ordered elements

import py5

def setup():
    py5.size(700, 980)
    py5.background(0, 0, 100)
    py5.no_stroke()

    cols = 10
    rows = 15
    offset_x = 50 # Margin from the left and right edges
    w = (py5.width - 2*offset_x) / cols
    offset_y = (py5.height - w*rows)/2 # Centering margin from top and bottom edges
    
    for j in range(rows):
        y = j * w + w/2 + offset_y
        for i in range(cols):
            # py5.rect(i*w, j*w, w, w)
            # py5.circle(i*w + w/2, j*w + w/2, w)
            x = i * w + w/2 + offset_x
            star(x, y, w/(2+0.3*j), w/6, 3+i)

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