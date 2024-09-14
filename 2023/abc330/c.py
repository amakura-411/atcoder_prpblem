import math
d = int(input())

ans = d
# +9するのは、誤差を考慮している
limit = int(d**0.5) + 9


for x in range(limit+1):
    yy = d - x**2
    if yy < 0: # yyは負の数のとき
        ans = min(ans, -yy)
    else: # 0以上の時
        y1 = int(yy ** 0.5) # yの平方根
        y2 = y1 + 1
        ans = min(ans, yy - y1**2, y2**2 - yy)



print(int(ans))