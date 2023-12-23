# 2
# 3 1 2
# 6 1 1

n = int(input())
sx = sy = st = 0
for i in range(n):
    t, x, y = map(int, input().split(" "))
    d = abs(x - sx) + abs(y - sy)
    time = t - st
    if d > time or d % 2 != time % 2:
        # 1秒後には到達できない場所を指定された場合
        # 偶奇の関係で到達できない場所を指定された場合
        print("No")
        exit()
    sx = x
    sy = y
    st = t
else:
    print("Yes")