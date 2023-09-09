n, h, k = map(int, input().split())
p = list(map(int, input().split()))
# print(p)
limit = k -h
for i in range(n):
    if p[i] >= limit:
        print(i+1)
        break;
