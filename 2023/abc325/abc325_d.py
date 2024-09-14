# ChatGPTと一緒に解いた
import heapq
ans = 0
n = int(input()) #商品数
time = []

for i in range(n):
    f, l = map(int, input().split(" ")) #はいる時間、出るまでの時間
    time.append([f, f +l])

# timeを出る時間でソート
# time.sort(key=lambda x: (x[1], x[0]))

time.sort()

p = [] #商品を入れる
num = 0 #現在の商品数
i = 0 #iにはいる時間を代入
while True:
    if not p: #pが空のとき
        if num == n: #商品数と同じになったら終了
            break
        i = time[num][0] #商品を入れる時間を代入

    while num < n and time[num][0] == i: #商品を入れる時間が同じなら
        heapq.heappush(p, time[num][1])
        num += 1 #商品数を増やす
    
    while p and p[0] < i: #商品が入っていて、出る時間が過ぎていたら
        heapq.heappop(p)

    if p: #商品が入っていたら
        heapq.heappop(p)
        ans += 1
    i += 1

print(ans)