from random import randint

def f(n):
    return -n

flowers = ["fialka", "romashka", "odyvanchik"]
colours = ["red", "green", "blue", "purple", "orange"]
colors_by_flowers = [colours[randint(0,len(colours)-1)] for  i in flowers]


# for i in range(len(colours)):
    
dic = dict(zip(flowers,colors_by_flowers_2))
print(dic)