# 3
# ooo
# oxx
# xxo

num = int(input())
row = [0] * num 
col =  [0] * num 
mass = [["" for _ in range(num)] for i in range(num)]
for i in range(num):
    m = input()
    for j in range(num):
        mass[i][j] = m[j]
        if mass[i][j] == "o":
            row[i] += 1
            col[j] += 1


ans = 0
for i in range(num):
    for j in range(num):
        if mass[i][j] == "o":
            ans += (row[i] - 1) * (col[j] - 1)
print(ans)


    
