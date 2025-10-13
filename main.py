num = int(input())
if num % 2 == 0:
    print("Чётное")
else:
    print("Не чётное")

chlen1 = int(input())
chlen2 = int(input())
chlen3 = int(input())
for i in range(chlen3 - 1):
    chlen1 = chlen1 * chlen2
print(chlen1)

year = int(input())
if (year % 4 == 0 && year % 100 != 0) | (year % 400 == 0):
    print("Год високосный")
else:
    print("Год невисокосный")

chislo_Fibonachi = int(input())
num2 = 1
num3 = 1
num4 = 0
for i in range(chislo_Fibonachi):
    print(num2)
    num4 = num2
    num2 = num3
    num3 = num4 + num3

cel1 = int(input())
cel2 = int(input())
ostatok = 0
chastnoy = 0
if cel2 == 0:
    print("Не делится")
else:
    ostatok = cel1 % cel2 
    chastnoy = cel1 // cel2 
print(ostatok, chastnoy)

for j in range(1,10):
    print()
    for i in range(1,10):
        print(i * j, end = '\t') 