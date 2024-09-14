num = int(input()) #人数
user_win = dict()# number:win
for i in range(1, num+1):
    user_win[i] = 0
    battle = input()
    for j in range(1, num+1):
        if i == j :  
            continue
        if battle[j-1] == "o":
            user_win[i] += 1

# 値で大きい順にソート。ただし。値が同じ場合はキーでソート（小さい順）
user_win = sorted(user_win.items(), key=lambda x: x[1], reverse=True)


for k, v in user_win:
    print(k, end=" ")
        

        
        
