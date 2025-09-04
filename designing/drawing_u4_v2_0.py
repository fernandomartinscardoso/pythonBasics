# Code to study designing using py5 library
# Based on the Domestika course "Designing with Python: Programming for a Visual Context" by Alexandre Villares
# This code is for Unit 4, Video 2 of the course.
# Theme: Export to PDF or SVG

import py5

save_document = False

def setup():
    py5.size(700, 980)

def draw():
    global save_document
    if save_document:
        # py5.begin_record(py5.SVG, 'output/drawing_u4_v2_0.svg')
        py5.begin_record(py5.PDF, 'output/drawing_u4_v2_0.pdf')
    py5.background(0, 100, 100)
    py5.circle(py5.width/2, py5.height/2, 500)
    if save_document:
        py5.end_record()
        save_document = False
        print('Document saved.')

def key_pressed():
    global save_document
    if py5.key == 'p':
        save_document = True
        print('Saving document...')

py5.run_sketch()
