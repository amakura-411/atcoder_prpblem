# 12
# 31 29 31 30 31 30 31 31 30 31 30 31


n = int(input())
d = list(map(int, input().split()))

month = 0
ans = 0
for i in range(1, n+1):
    month = i
    num = month % 10
    if num == 0:
        continue
    if month //num == 1 or month // num == 11:
        for day in range(1, d[i-1]+1):
            if day / num == 1 or day / num == 11:
                ans += 1
                # print(month, day, num)

print(ans)