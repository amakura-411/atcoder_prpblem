# 6 1
# 112022
n, m = map(int, input().split(" "))
s = input()

r = 0
b = 0
ans = 0
max_num = 0
# ０までの間に何回２が出てくるか
for i in range(n):
    if s[i] == "0":
        # 何の予定も入っていません
        # 着用済みの T シャツを全て洗濯
        num = m - b
        if num > 0:
            num = 0
        max_num = max(max_num, r - num)
        r = 0
        b = 0
    elif s[i] == "1":
        # 高橋君は食事に行く予定
        # 無地の T シャツ 1 枚またはロゴ入りの T シャツ 1 枚を着用
        b += 1
    elif s[i] == "2":
        # 高橋君は競技プログラミングのイベントに行く予定
        # ロゴ入りの T シャツ
        r += 1
    
num = m - b
if num > 0:
    num = 0
max_num = max(max_num, r - num)

print(max_num)

