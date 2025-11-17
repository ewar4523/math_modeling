def gdz(choise, a, b, c):
    pi = 3.14
    if choise == 1:
        S = a**2 * pi
        return S 
    elif choise == 2:
        S1 = 0.5 * a * b
        return S1
    elif choise == 3:
        S2 = a * b
        return S2

choise = int(input())
a = int(input())
b = int(input())
c = int(input())
print(gdz(choise, a, b, c))