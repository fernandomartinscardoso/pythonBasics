# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 6 of the course.
# Theme: define and use new functions

import py5

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(0, 0, 200) # Dark blue background
    for y in range(100, 1000, 100):
        eye(py5.width/2, y, 150)

def eye(x, y, w):
    py5.no_stroke()
    py5.fill(255)
    py5.ellipse(x, y, w, w/3)
    py5.fill(0, 200, 0)
    py5.ellipse(x, y, w/3, w/3)
    py5.fill(0)
    py5.ellipse(x, y, w*0.1, w*0.1)

py5.run_sketch() # Run the sketch to see the setup and draws applied.