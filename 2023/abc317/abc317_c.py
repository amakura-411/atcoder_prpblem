#解説確認済
from collections import deque
n, m = map(int, input().split())
loads = dict()

for i in range(m):
    a, b, c = map(int, input().split())
    if a not in loads:
        loads[a] = []
    if b not in loads:
        loads[b] = []
    loads[a].append([b, c])
    loads[b].append([a, c])

visited = [False for _ in range(n+1)]


ans = 0

def dsf(start, distance):
    visited[start] = True
    global ans
    if distance > ans: ans = distance #最大値を更新する
    for i in loads[start]:
        if i and i not in visited: 
            dsf(i[0], distance)
    visited[start] = False

for i in range(1, n+1):
    dsf(i, 0)   

print(ans)






