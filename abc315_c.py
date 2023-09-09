#n個のアイスがある。
#このアイスのi番目のフレーバーはfであり、これを食べるとsの幸福度を得る
#ただし、fが重複する場合、幸福度は、２番目のものは半分となる。
#この時の最適解を求めよ。
#なお、nこのうち選べるのは2個のみである。
#入力
n = int(input()) #個数
#フレーバーはn個あるので、n個のリストを作成する
#likes = []
ice = [[0]*2 for i in range(n)] 

for i in range(n):
    ice[i][0], ice[i][1] = map(int, input().split())

#sの大きい順にソートする
ice.sort(key=lambda x: x[1], reverse=True)

# print(ice)
happiness = 0
max_s = ice[0][1] #10
# for i in likes:
#　幸福度が最大となるペアを探す。
# print(ice[0][1])
ans = 0
max_count = 0
for i in range(2):
    if max_s > ice[i][1]:
        #2回目のループで、最大値が更新されなかった場合は、breakする。
        break
    # print(ice[i])s
    # max_count += 1
    for j in range(i+1, n):
        # print(ice[i], ice[j])
        if ice[j][1] <= ans:
            #現状の最大値よりhappinessが小さくなった段階でbreakする。
            break        
        happiness = ice[j][1]
        if ice[i][0] == ice[j][0]:
            happiness = happiness // 2
            same_f = 1
        ans = max(ans, happiness)





print(ans+max_s)
    