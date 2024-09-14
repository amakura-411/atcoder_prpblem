n, m ,x = map(int, input().split(" "))

# 3 3 10
# 60 2 2 4
# 70 8 7 9
# 50 2 3 9
# price, understand, understand, understand * n

prices = []
understands = []
for i in range(n):
    price, *understand = map(int, input().split(" "))
    prices.append(price)
    understands.append(understand)

# 購入するかどうかをbit全探索
ans = float('inf')
for i in range(1<<n):
    # 000 001 010 011 100 101 110 111...
    sum = 0
    status = [0] * m
    for j in range(n):
        if (i>>j) & 1 == 0: continue # 購入しない
        # 購入するとき
        sum += prices[j]
        for k in range(m):
            status[k] += understands[j][k]
        # もし、全ての理解度がx以上なら
        if all([x <= s for s in status]):
            ans = min(ans, sum)
if ans == float('inf'):
    print(-1)
else:
    print(ans)

