# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 7 of the course.
# Theme: Function to draw stars

import py5

def setup():
    py5.size(980, 980)
    py5.background(0, 0, 200)
    star4(300, 300, 200, 40)
    star(600, 600, 150, 50, 11)

def star4(xc, yc, wa, wb):
    pts = [(-wa, -wa), (0, -wb), (wa, -wa), (wb, 0), (wa, wa), (0, wb), (-wa, wa), (-wb, 0)]
    py5.begin_shape() # begin_shape() and end_shape() are used to create complex shapes by defining a series of vertices.
    for x, y in pts:
        py5.vertex(x + xc, y + yc) # vertex(x, y) defines a vertex at position (x, y) to be used in conjunction with begin_shape() and end_shape().
    py5.end_shape(py5.CLOSE) # The parameter CLOSE connects the last vertex to the first, closing the shape.

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