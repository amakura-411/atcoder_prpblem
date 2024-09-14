# 3
# 0 5 1 3
# 1 4 0 5
# 2 5 2 4

def addmass(mass, a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            mass[i][j] += 1
    return mass


n = int(input())

mass = [[0 for i in range(100)] for j in range(100)]
for i in range(n):
    a, b, c, d = map(int, input().split())
    # a-bは横
    # c-dは縦
    # print(a, b, c, d)
    mass = addmass(mass, a, b, c, d)


# massのうち、1以上の数をカウントする
count = 0
for i in range(100):
    for j in range(100):
        if mass[i][j] >= 1:
            count += 1
print(count)

