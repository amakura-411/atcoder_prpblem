# 1 2 3 4 5 6 7 8 9
# 4 5 6 7 8 9 1 2 3
# 7 8 9 1 2 3 4 5 6
# 2 3 4 5 6 7 8 9 1
# 5 6 7 8 9 1 2 3 4
# 8 9 1 2 3 4 5 6 7
# 3 4 5 6 7 8 9 1 2
# 6 7 8 9 1 2 3 4 5
# 9 1 2 3 4 5 6 7 8

from collections import defaultdict

mass = [[0]*9 for i in range(9)]

np = defaultdict(set)
row = [set() for i in range(9)]
col = [set() for i in range(9)]

ans = "Yes"
for i in range(9):
    s = list(map(int, input().split(" ")))
    for j in range(9):
        mass[i][j] = s[j]
        np[(i//3, j//3)].add(s[j])
        row[i].add(s[j])
        col[j].add(s[j])

for i in range(9):
    for j in range(9):
        if len(np[(i//3, j//3)]) != 9:
            ans = "No"
            break
        if len(row[i]) != 9:
            ans = "No"
            break
        if len(col[j]) != 9:
            ans = "No"
            break

print(ans)



