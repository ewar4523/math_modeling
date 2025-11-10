import numpy as np
from math import *


N = int(input())
M = int(input())
masivy = np.zeros((N, M))
masivy1 = np.zeros((N, M))

for i in range(len(masivy)):
    for j in range(len(masivy[i])):
        masivy[i][j] = sin(N * i + M * j + 1)
print(masivy)


for i in range(len(masivy)):
    # for j in range(len(masivy[i])):
        t = masivy[i,0]
        masivy[i,0] = masivy[i,1]
        masivy[i,1] = t

print(masivy)