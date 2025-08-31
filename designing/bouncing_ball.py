# Bouncing ball example using py5 library
# Adapted from https://cratecode.com/info/py5-animations

import py5
from random import randint

def setup():
    py5.size(980, 980)

d = 70 # diameter of the ball
width, height = 980, 980
x, y = randint(int(d/2), int((width-d/2))), randint(int(d/2), int((height-d/2))) # start position
x_speed, y_speed = 6, 10  # speed in x and y direction

def draw():
    global x, y, x_speed, y_speed, d
    py5.background(200)
    py5.fill(0)
    py5.ellipse(x, y, d, d)

    x += x_speed
    y += y_speed

    # Bounce off edges
    if x > py5.width - int(d/2) or x < int(d/2):
        x_speed *= -1
    if y > py5.height - int(d/2) or y < int(d/2):
        y_speed *= -1


py5.run_sketch() # Run the sketch to see the setup and draws applied.