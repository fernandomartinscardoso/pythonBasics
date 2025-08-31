"""
This example shows:
- "for" loop for drawing a sequence of elements
- random_int() for selecting an integer number
- random_choice() for selecting from a collection of items
- random_seed(0 for fixing the random generator starting point
- if/elif/else conditional structure for deciding which shape to draw
- A n-pointed star function definition you can use: star()
"""

def setup():
    size(600, 600)
    background(200)
    no_stroke()
    fill(0)
    # set the random generator starting point with random_seed()
    random_seed(100)  # change this or comment out for different results
    for x in range(50, 600, 100):  # x -in loop-> 50, 150, 250, 350, 450, 550
        n = random_int(1, 7)             # n -random-> 1, 2, 3, 4, 5, 6, 7
        r = random_choice((10, 25, 40))  # r -random-> 10, 25, 40
        if n == 1:   # if n equals 1:
            circle(x, 300, 50)       # x, y, diameter    
        elif n == 2: # else if n equals 2:
            square(x - 25, 300 - 25, 50) # I could have used rect_mode(CENTER)!
        else:  # else, n is not 1 nor 2, then:
            star(x, 300, r, 50, n)   # x, y, radius_a, radius_b, num_of_points
        

def star(cx, cy, ra, rb, n, start_ang=0):  # "estrela"
    step = TWO_PI / n   # 360° / number of star (outer) points
    begin_shape()       # start poly shape
    for i in range(n):  # for each tip/point
        ang = start_ang + step * i # angle used to calculate vertex position
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)  # add vertex calculated from radius ra
        bx = cx + cos(ang + step / 2.0) * rb  # note half steo added to angle
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)  # add vertex calculated from raidius rb
    end_shape(CLOSE)    # end poly shape, and connect to first vertex
        
        
        
        
        