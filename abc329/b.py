# 5
# 2 1 3 3 2

n = int(input())
a = list(map(int, input().split()))

max_num = max(a)
ans = 0
for i in range(n):
    if a[i] == max_num:
        continue    
    ans = max(ans, a[i])
print(ans)
