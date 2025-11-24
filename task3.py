import time

timer = time.time()

m = int(input())
n = int(input())

for i in range(m):
    print(i)
    time.sleep(1)
    for j in range(n):
        print(j)
        time.sleep(1)

print(f'{time.time()-timer}')