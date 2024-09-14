import collections
# 11 4
# mississippi
# 00011122233
# 3 9
# 4 10
# 4 6
# 7 7

n, q = map(int, input().split())
s = input()
count = [0] * (n+1)
prev = s[0]
print(s)
print(count)

for i in range(1, n):
    count[i] = count[i-1]
    if s[i] == prev :
        count[i] += 1
    prev = s[i]
print(count)

for i in range(q):
    l, r = map(int, input().split())
    print(count[r-1] - count[l-1])