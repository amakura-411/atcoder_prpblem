# 5 180
# 40 60 80 50
n, x = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
sums = sum(s)

ans = 102

for i in range(101):
    num = sums - s[0] - s[-1]
    if i <= s[0]:
        num += s[0]
    elif i >= s[-1]:
        num += s[-1]
    else:
        num += i
    if num == x:
        ans = min(ans, i)

if ans == 102:
    ans = -1


print(ans)
