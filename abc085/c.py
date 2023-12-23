# 9 45000

# 10000 円札、
# 5000 円札、
# 1000 円
n, price = map(int, input().split(" "))
for i in range(n+1):
    for j in range(n+1-i):
        if price == 10000 * i + 5000 * j + 1000 * (n-i-j):
            print(i, j, n-i-j)
            exit()
else:
    print(-1, -1, -1)