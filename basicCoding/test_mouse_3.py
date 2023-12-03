# Mouse describing a circle
# Center of the circle: (650,400)
# Radius of the circle: 150

x1 = []
for i in range(500,801):
    x1.append(i)

x2 = []
for j in range(800,499,-1):
    x2.append(j)

y1 = []
for k in range(len(x1)):
    y1.append(round((150**2-(x1[k]-650)**2)**(1/2)+400))

y2 = []
for l in range(len(x2)):
    y2.append(round(-(150**2-(x2[l]-650)**2)**(1/2)+400))

x = x1 + x2
y = y1 + y2

import time
import mouse

for n in range(30):
    for m in range(len(x)):
        mouse.move(x[m],y[m],absolute=True,duration=0)
        time.sleep(0.01)
        
    
