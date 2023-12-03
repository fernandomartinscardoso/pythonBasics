'''
Visualizing the Möbius Strip in Python
by MathCube at https://medium.com/@mathcube7/visualizing-the-m%C3%B6bius-strip-in-python-3c086ad9fb32

One possible parametrization of the Möbius Strip is given by

x = (1 + (v/2)cos(u/2))cos(u)
y = (1 + (v/2)cos(u/2))sin(u)
z = (v/2)sin(u/2)

for u in the range of 0 and 2pi and v in the range -1 to 1.

Other references:
https://en.wikipedia.org/wiki/M%C3%B6bius_strip
https://github.com/oguzhankir/SHORTS_ENG/tree/main/m%C3%B6bius_strip

'''

#import packages

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#intervals required to construct axes

u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(-1, 1, 30)

u, v = np.meshgrid(u, v, sparse=True)
U, V = np.meshgrid(u, v, sparse=False)

#parametrization

x = (1+v/2*np.cos(u/2))*np.cos(u)
y = (1+v/2*np.cos(u/2))*np.sin(u)
z = v/2*np.sin(u/2)

#plot part

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm,
                      linewidth=0.1, antialiased=False)

ax.xaxis.set_major_locator(LinearLocator(10))
ax.xaxis.set_major_formatter("{x:.02f}")

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
