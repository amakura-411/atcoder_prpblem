import math
m = int(input()) #月
day = list(map(int, input().split())) #日
#print(day.count(m))
#１年の中央値は何月何日化を求めるコード
#１年はdayの合計値
#dayの合計値を2で割ったときの値が中央値
#中央値が何月何日かを求める

# 1年の中央値を求める
sum_days = sum(day)
print(sum_days)
# 切り上げ
center = math.ceil(sum_days / 2)
ans_m = 0
ans_d = 0
sums = 0;
while  sums < center:
    ans_m += 1
    if sums + day[ans_m -1] < center:
        #もし。合計値と当月日数が中央値よりも小さい場合は。
        sums += day[ans_m - 1]
    elif sums + day[ans_m - 1] >= center:
        #もし。合計値と当月日数が中央値よりも大きい場合は。
        ans_d = center - sums
        break


# 6
# 3 1 4 1 5 9

# 0 < 23/2


print(ans_m, ans_d)
