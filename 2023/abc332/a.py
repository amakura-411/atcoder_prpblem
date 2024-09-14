# 2 2000 500
# 1000 1
# 100 6
n,s,k = map(int,input().split())
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    ans += a*b

if ans < s:
    ans += k
print(ans)
