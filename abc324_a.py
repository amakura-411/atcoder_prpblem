# 3
3 2 4

n = int(input())
a = list(map(int, input().split()))
# 全て同じ数字であるかどうか
ans = True
for i in range(n-1):
    if a[i] != a[i+1]:
        ans = False
        break

if ans == True:
    print("Yes")
else:

