N, L = map(int, input().split(" "))
ans = 0
a = list(map(int, input().split(" ")))
for i in range(N):
    point = a[i]
    if point >= L:
        ans += 1


print(ans)