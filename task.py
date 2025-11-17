import numpy as np

def sr_mas(mas):
    sum = 0
    sr = 0
    for i in range(len(mas)):
        sum = sum + mas[i]
    sr = sum / len(mas)
    return sr

a = np.array([1,2])
print(sr_mas(a))
