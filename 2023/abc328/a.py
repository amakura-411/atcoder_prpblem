# 6 200
# 100 675 201 200 199 328

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i]>k:
        continue
    ans += a[i]

print(ans)


