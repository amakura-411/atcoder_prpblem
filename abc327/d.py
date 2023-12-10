# 3 3
# 1 2 3
# 2 3 1

n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

ans = "Yes"
for i in range(n):
    if (a[i] + b[i]) % 2 == 0:
        ans = "No"
        break
print(ans)
