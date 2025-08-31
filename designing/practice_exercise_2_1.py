# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 2.1
# Student: Fernando Cardoso
# Date: 31.08.2025
# Tasks:
# Make a drawing with the elements presented in the course: rectangles, circles, polygons, eye and star.
# Identify the ones you like best and choose RGB colors for the fill (fill()) and outline (stroke()), 
# or use them without fill (no_fill()) or without an outline (no_stroke()), positioning them on the screen 
# in an interesting composition.

import py5

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(128, 200, 255) # Light blue background

    eye(py5.width/2, py5.height/2, 500)
    py5.fill(200, 200, 0)
    py5.stroke(0)
    py5.square(49, 49, 98)
    py5.square(833, 49, 98)
    py5.square(49, 833, 98)
    py5.square(833, 833, 98)
    for i in range(1,8):
        if i <= 4:
            star(98 + i*98, 98, 30, 15, i+3, py5.HALF_PI)
            star(98, 98 + i*98, 30, 15, i+3, py5.HALF_PI)
            star(98 + i*98, 882, 30, 15, i+3, py5.HALF_PI)
            star(882, 98 + i*98, 30, 15, i+3, py5.HALF_PI)
        else:
            star(98 + i*98, 98, 30, 15, 11-i, py5.HALF_PI)
            star(98, 98 + i*98, 30, 15, 11-i, py5.HALF_PI)
            star(98 + i*98, 882, 30, 15, 11-i, py5.HALF_PI)
            star(882, 98 + i*98, 30, 15, 11-i, py5.HALF_PI)



def eye(x, y, w):
    py5.no_stroke()
    py5.fill(255)
    py5.ellipse(x, y, w, w/3)
    py5.fill(0, 200, 0)
    py5.ellipse(x, y, w/3, w/3)
    py5.fill(0)
    py5.circle(x, y, w/5)
    py5.fill(128, 75, 0)
    star(x, y, w/12, w/24, 6, py5.HALF_PI)

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
py5.save_frame('practice_exercise_2_1.png') # Save a snapshot of the sketch window as a PNG file.
