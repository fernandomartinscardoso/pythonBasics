"""
This example shows:
- How to define a function that draws an eye and how to use this function
- Programming vocabulary:
     - "call" a function, "pass values or arguments"
     - "header" and "body" of a function definition
     - "parameters", names designated in the function definition
"""

def setup():
    size(600, 600)
    background(0, 0, 100)
    eye(200, 150, 100)  # calling the eye function (to draw an eye)
     eye(300, 400, 150) # <- values (arguments) passed to x, y and h inside eye 
     eye(500, 200, 50)  # when we call a function its name has parentheses
                        # which may or may not need arguments
                        # fill(255) <- 255 is the "passed" argument
                        # no_fill() <- no_fill function takes no arguments
   
#       x, y, h       <- these are the parameter names (that get the values)
def eye(x, y, h):   # <- this is the "header"  of the eye definition
    no_stroke()     # <- here starts the function's "body" (note indentation)              
    fill(255)       # white fill       
    ellipse(x, y, h * 3, h)
    fill(255, 0, 0) # red fill
    ellipse(x, y, h, h)
    fill(0)         # black fill
    ellipse(x, y, h * 0.2, h * 0.2)
#                     <-  here the eye function's "body" ends