# Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# Practice exercise 2.2
# Student: Fernando Cardoso
# Date: 31.08.2025
# Tasks:
# Create a composite graphic/visual element. Define a function that draws these instructions and post it to the forum.
# Use its function to make a composition with 3 or more examples of the element.

import py5

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(128, 200, 128)
    concentric_circles(3*py5.width/4, py5.height/4, 15, 650)
    concentric_circles(py5.width/4, py5.height/4, 25, 650)
    concentric_circles(3*py5.width/4, 3*py5.height/4, 15, 650)
    concentric_circles(py5.width/4, 3*py5.height/4, 20, 650)

def concentric_circles(x, y, n, d):
    # Draws n concentric circles centered at (x, y) with a maximum diameter d.
    py5.no_fill()
    py5.stroke(0)
    for i in range(n):
        py5.circle(x, y, d - i * d/n)


py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_2_2.png') # Save a snapshot of the sketch window as a PNG file.
