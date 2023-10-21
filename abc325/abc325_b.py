def add_count(counts, t, m):
    a = t + 9
    for i in range(9):
        counts[(a+i)%24] += m
    return counts

n = int(input()) #拠点数
#9:00-18:00 の期間中の場合のみ 加算される
member = list()
time = list()
counts = [0 for i in range(24)]
for i in range(n):
    m, t = map(int, input().split()) #拠点にいる人数 世界標準を０とした時の拠点の時刻
    add_count(counts, t, m)

# countsの中の最大値を求める
print(max(counts))

print(counts) 


