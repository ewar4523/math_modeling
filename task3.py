import numpy as np
from constants import g

Vx = int(input())
Vy = int(input())
x0 = int(input())
y0 = int(input())
t = np.arange(0, 5.25, 0.25)

x = x0 + Vx * t
y = y0 + Vy * t - (g * (t ** 2)) / 2 

array = np.zeros((len(t), 3))
array[::, 1] = x
array[::, 2] = y
array[::, 0] = t
print(array)
