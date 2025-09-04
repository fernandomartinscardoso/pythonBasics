# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercises 4.1 and 4.2
# Student: Fernando Cardoso
# Date: 03.08.2025
# Tasks:
# 4.1. Consider whether your project would benefit from having smaller grids within the grid, and elements at various scales. 
# Try to apply what you saw in this unit about recursion to your poster.
# 4.2. Adapt the export examples in vector formats for your project, and produce some sample PDFs for your portfolio!

import py5
from random import randint, seed

save_document = False # Variable to control saving the document
s = 1 # Seed for random number generator

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(693, 980)

def draw():
    global s, save_document
    py5.begin_record(py5.PDF, f'output/poster_4_2_{s}.pdf')
    seed(s)
    py5.background(70, 70, 0)
    for _ in range(3):
        grid(4, 6, 50, 40, 600)
    py5.end_record()
    if s == 20:
        py5.exit_sketch()
    s += 1  # Increment seed for next draw

def grid(cols, rows, offset_x, offset_y, wt):
    py5.stroke(255)
    # cols is number of columns
    # rows is number of rows
    # offset_x is the margin from the left and right edges
    w = wt / cols
    for j in range(rows):
        y = j * w + w/2 + offset_y
        r = randint(0, 128)
        g = randint(0, 255)
        b = randint(0, 255)
        py5.fill(r, g, b)
        for i in range(cols):
            x = i * w + w/2 + offset_x
            m = randint(1, 6)
            if m <= 2:
                concentric_circles(x, y, randint(1,4), w-5*randint(0,5))
            elif 2 < m <= 5:
                py5.fill(randint(0, 128), 150)
                dr = randint(0, 1)*w/2
                py5.rect(x-dr, y-dr, w/2, w/2)
            else:
                py5.fill(randint(0, 128), randint(0, 128), randint(0, 150), 150)
                ra = randint(5, int(w/2))
                rb = randint(5, int(w/2))
                np = randint(4, 10)
                star(x, y, ra, rb, np)
            if randint(1, 3) == 3 and w > 30:
                grid(2, 2, x-w/2, y-w/2, w)

def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.stroke(0)
    for i in range(n):
        py5.fill(randint(0, 128), randint(0, 128), randint(0, 150), 150)
        py5.circle(x, y, d - i * d/n)

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
