import numpy as np

def ymnogeny(mas):
    ravno = mas[0]
    for i in range(len(mas)):
        ravno = ravno * mas[i]
    return ravno

a = np.array([1,3,6,2])
print(ymnogeny(a))
