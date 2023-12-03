import mouse

a = mouse.get_position()

print('Mouse position is {}'.format(a))

# mouse.drag(2700,200,2900,250, absolute=True, duration=5)
mouse.move(100,100,absolute=False,duration=2)