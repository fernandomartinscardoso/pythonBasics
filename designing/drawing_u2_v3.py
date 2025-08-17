# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 3 of the course.

import py5

def setup():
    """
    Initializes the sketch window and sets up the drawing environment.
    """
    py5.size(980, 980)

def draw():
    """
    Draw environment function.
    """
    py5.ellipse(py5.mouse_x, py5.mouse_y, 50, 50)

py5.run_sketch()
