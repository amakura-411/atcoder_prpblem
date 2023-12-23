# 4 5
# 1 10 100 1000

n, x = map(int, input().split())
a = list(map(int, input().split(" ")))

# 5 = 0101
ans = 0
for i in range(n):
    if (x>>i)&1:
        ans += a[i]
print(ans)
