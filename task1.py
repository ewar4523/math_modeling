import random as r


dlina = int(input())
a = [r.randint(1,100) for i in range(dlina)]
b = [r.randint(1,100) for i in range(dlina)]
c = [r.randint(1,100) for i in range(dlina)]


modul = [max(a), max(b), max(c)]
print(max(modul))