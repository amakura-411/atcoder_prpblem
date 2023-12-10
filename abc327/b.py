import math
n = int(input())
num = 0
for i in range(1, 10**18):
    num = i**i
    if num > n:
        print(-1)
        break
    elif num == n:
        print(i)
        break
