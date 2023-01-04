# -*- coding: utf-8 -*-
"""
Exemplo de uso de plot com python retirado de 
https://pythonspot.com/matplotlib-scatterplot/
Ver tambem:
https://pythonspot.com/matplotlib/
"""

import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.8)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()