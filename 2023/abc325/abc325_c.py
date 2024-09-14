# 右、下、左、上、右下、右上、左下、左上
H, W = map(int, input().split())
def change_true(block, flag, i, j):
    if block[i][j] == "." or flag[i][j] == True:
        flag[i][j] = True
        return flag, 0
    
    next_pop = list()
    next_pop.append([i, j])

    while len(next_pop) > 0:
        i, j = next_pop.pop()
        # print(next_pop)
        if flag[i][j] == True:
            continue
        # print(i, j, block[i][j])
        if j > 0: #右端ではない場合
            if block[i][j-1] == "#":
                next_pop.append([i, j-1])
        if j < W-1: #左端ではない場合
            if block[i][j+1] == "#":
                next_pop.append([i, j+1])
        if i > 0: #上端ではない場合
            if block[i-1][j] == "#":
                next_pop.append([i-1, j])
        if i < H-1: #下端ではない場合
            if block[i+1][j] == "#":
                next_pop.append([i+1, j])
        if i > 0 and j > 0: #右上端ではない場合
            if block[i-1][j-1] == "#":
                next_pop.append([i-1, j-1])
        if i < H-1 and j < W-1: #左下端ではない場合
            if block[i+1][j+1] == "#":
                next_pop.append([i+1, j+1])
        if i > 0 and j < W-1: #右下端ではない場合
            if block[i-1][j+1] == "#":
                next_pop.append([i-1, j+1])
        if i < H-1 and j > 0: #左上端ではない場合
            if block[i+1][j-1] == "#":
                next_pop.append([i+1, j-1])
        flag[i][j] = True
    return flag, 1








block = [["" for i in range(W)] for j in range(H)]
flag = [[False for i in range(W)] for j in range(H)]

for i in range(H):
    s = input()
    for j in range(W):
        block[i][j] = s[j]


ans = 0
for i in range(H):
    for j in range(W):
        flag, count  = change_true(block, flag, i, j)
        ans += count

print(ans)



