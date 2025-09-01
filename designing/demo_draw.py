# Demonstration of drawing interations in py5

import py5
from random import randint, seed

s = 10 # Seed for random number generator

def setup():
    py5.size(980, 980)
    py5.no_loop() # Disable continuous drawing

def draw():
    py5.background(200)
    seed(s) # Set the seed for reproducibility
    d = randint(100, 200)
    py5.fill(randint(0, 255), randint(0, 255), randint(0, 255))
    py5.circle(py5.width/2, py5.height/2, d)

def mouse_pressed():
    global s
    s += 1
    print(s)
    py5.redraw() # Redraw the canvas on mouse press

py5.run_sketch() 
