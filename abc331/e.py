from collections import defaultdict

n, m, l = map(int, input().split())

s_price = list(map(int, input().split()))
h_price = list(map(int, input().split()))

ans = 0
# 食い合わせ
k = defaultdict(set)
for _ in range(l):
    c, d = map(int, input().split())
    k[c-1].add(d)

# sort
h_price = list(enumerate(h_price, 1))
h_price = sorted(h_price, key=lambda x: x[1], reverse=True)

for i in range(n):
    for j, sub_price in h_price:
        # print("i:", i, "sub_price:", sub_price)
        if j not in k[i]:
            # print("i:", i, "not in k[index]:", k[index])
            ans = max(ans, s_price[i] + sub_price)
            # print("ans:", ans)
            break

print(ans)
