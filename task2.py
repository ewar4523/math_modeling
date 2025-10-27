import numpy as n
from constants import *
h = 100 
a = 45
B = 35
v = ((g * h * n.tan(B)**2) / (2 * n.cos(a)**2 * (1 - n.tan(B) * n.tan(a)))) ** 0.5
print(v) 

T = 200
e = 200
N = (2 / pi ** 0.5) * Planka ** 0.5 * ((k * T) ** 3/2) * e** E/k*T * E ** T/2 
print(N)