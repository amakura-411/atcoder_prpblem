from collections import defaultdict
# 4
# 3
# 7 19 20
# 4
# 4 19 24 0
# 2
# 26 10
# 3
# 19 31 24
# 19

n = int(input())

# 何番目とかけた数
# メンバーの番号とそのメンバーがかけた数
member = defaultdict(int)

mass = defaultdict(set)
for i in range(n):
    member[i] = int(input())
    a = list(map(int, input().split()))
    for j in range(member[i]):
        mass[a[j]]

print(mass)
print(member)

# memberを降順にソート
member = sorted(member.items(), key=lambda x: x[1], reverse=True)
print(member)





