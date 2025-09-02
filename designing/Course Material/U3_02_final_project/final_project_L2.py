
def setup():
    size(700, 980)
    background(0, 0, 100)
    no_stroke()
    fill(255)
    cols = 10
    rows = 15
    off_x = 50
    w = (width - 2 * off_x) / cols
    off_y = (height - w * rows) / 2  # margin v
    for j  in range(rows):
        y = off_y + j * w + w / 2
        for i in range(cols):
            x = off_x + i * w + w / 2
            star(x, y, w / (2 + j), w / 6, 3 + i)
                

def star(cx, cy, ra, rb, np, start_ang=0):  # estrela
    step = TWO_PI / np  # passo
    begin_shape()
    for i in range(np):  # for each tip/point
        ang = start_ang + step * i # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)
    
