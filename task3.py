from constants import g

def mex_sila(masa,vysota,skoroste):
    E = (masa * vysota * g) + ((masa * skoroste ** 2) / 2)
    return E

print("Порядок ввода: масса, высота, скорость")
a = int(input())
b = int(input())
c = int(input())
print(mex_sila(a,b,c))