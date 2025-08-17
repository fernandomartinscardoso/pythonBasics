# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 2, Video 4 of the course.

import py5

# Initializes the sketch window and sets up the drawing environment.
def setup():
    py5.size(980, 980)
    py5.background(200, 0, 200) # Set the background color. Each number represents RGB values (from 0 to 255).
    py5.rect_mode(py5.CENTER) # If you use rect_mode(py5.<mode>), you can change how the rectangle is drawn. The mode py5.CENTER, for example, turns the center of the rectangle the new reference to draw it.
    py5.fill(0, 200, 0) # Set the fill color for shapes. Always use it before drawing the shape, otherwise it will not be applied.
    # py5.no_stroke() # Disable the outline of shapes. If you want to draw a shape without an outline, use no_stroke() before drawing it.
    py5.stroke(255, 0, 0) # Set the stroke color for shapes. If you want to draw a shape with an outline, use stroke() before drawing it.
    py5.stroke_weight(10) # Set the thickness of the outline. The number is the thickness in pixels.
    py5.rect(py5.width/2, py5.height/2, 200, 50) # rect(x,y,w,h) draws a rectangle at position (x,y) with width of w pixels and height of h pixels.
    # py5.width and py5.height are the dimensions of the window, so py5.width/2 and py5.height/2 will center the rectangle in the window.
    # Notice that position (0,0) is the top-left corner of the window, and the y-axis increases downwards.
    py5.no_stroke() # Disable the outline of shapes for the next shape.
    py5.fill(255) # if all the values are the same, it will be a shade of gray from black (0) to white (255).
    py5.ellipse(200, 200, 300, 100) # ellipse(x,y,w,h) draws an ellipse centered at position (x,y) with width of w pixels and height of h pixels.

py5.run_sketch() # Run the sketch to see the setup and draws applied.