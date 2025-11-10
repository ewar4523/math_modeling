from math import *
import numpy as np

N = int(input())
M = int(input())
masivy = np.zeros((N, M))
masivy1 = np.zeros((N, M))

for i in range(len(masivy)):
    for j in range(len(masivy[i])):
        masivy[i][j] = sin(N * i + M * j + 1)

print(masivy)