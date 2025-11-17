import numpy as np

def fun(a, b, N):
    arr2 = (np.linspace(a, b, N)) ** 2
    return arr2

print("Напишите промежуток a<x<b в точках N")
a = int(input())
b = int(input())
N = int(input())
print(fun(a,b,N))
