from collections import defaultdict
# 5 9
# 2 3 :3
# 1 U
# 2 3 :4
# 1 R 
# 1 D 
# 2 3 :5
# 1 L
# 2 1
# 2 5
n, q = map(int, input().split())
# *****

# 構造して、x,y,countを持つデータを作る
# dragon= {count =  [x,y]}
dragon = defaultdict(list)
for i in range(1, n+1):
    dragon[i] = [n-i+1, 0]

# print(dragon)
top = n
x = 1
y = 0
# top: 5, 0
# print(top, ':x->', x, ',y->', y)
for i in range(q):
    query, c = map(str, input().split())
    if query == "1":
        # 移動
        if c == "U":
            y += 1
        elif c == "D":
            y -= 1
        elif c == "R":
            x += 1
        elif c == "L":
            x -= 1
        # 位置を更新
        top += 1
        dragon[top] = [x, y]
    elif query == "2":
        # 確認
        p = int(c) 
        # print(dragon, top, p, top-p)
        print(dragon[top-p+1][0], dragon[top-p+1][1])
