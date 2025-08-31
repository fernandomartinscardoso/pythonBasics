# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 5 of the course.
# Theme: repeat loops to create patterns with lines.

import py5

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(240)
    
    for n in range(10, 70, 2):
        py5.line(n*10, 100, n*3, 490) # line(x1, y1, x2, y2) draws a line from point (x1, y1) to point (x2, y2).
    
    margin = 50
    for i in range(20):
        py5.line(margin + i*8, 150, margin + i*16, 600)

py5.run_sketch() # Run the sketch to see the setup and draws applied.