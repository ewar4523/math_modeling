def fib(n):
    fibonachi = 0
    fibonachi1 = 1
    for i in range(n -1):
        tmp = fibonachi
        fibonachi = fibonachi1
        fibonachi1 = fibonachi1 + tmp
    return fibonachi

print(fib(7))