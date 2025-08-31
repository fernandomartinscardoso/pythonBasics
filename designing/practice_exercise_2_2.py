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

def concentric_circles(x, y, n, d):
    
    py5.no_fill()
    py5.stroke(0)
    for i in range(n):
        py5.circle(x, y, d + i * d)


py5.run_sketch() # Run the sketch to see the setup and draws applied.
py5.save_frame('practice_exercise_2_2.png') # Save a snapshot of the sketch window as a PNG file.
