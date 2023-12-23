# erasedream
# T の末尾に dream dreamer erase eraser のいずれかを追加する。

S = input()
num = len(S)
while(num > 0):
    # print(S[num-7:num], S[num-5:num])
    if S[num-7:num] == 'dreamer':
        num -= 7
    elif S[num-6:num] == 'eraser':
        num -= 6
    elif S[num-5:num] == 'dream' or S[num-5:num] == 'erase':
        num -= 5
    else:
        print('NO')
        exit()
else:
    print('YES')    
    # if S[num:num+5] == 'dream':
    #     num += 5

