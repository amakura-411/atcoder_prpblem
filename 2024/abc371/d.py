import bisect


# 数直線上に N 個の村があります。
# i 番目の村は座標 Xiにあります。
# i番目の村の人口は Pi人です。

# 座標が L i​以上 R i以下の村に住んでいる村人の人数の総数
N = int(input())  # 村の数

# 村の座標
X = list(map(int, input().split(' ')))
# 村の人口
P = list(map(int, input().split(' ')))
# クエリの数
Q = int(input())

# 事前に人口を計算し、２分探索とかで範囲を求めて、その範囲内の人口を足し合わせる
people = [0] * (N+1)
for i in range(N):
  people[i+1] = people[i] + P[i]

for i in range(Q):
  L, R = map(int, input().split(' '))
  # ２分探索
  left = bisect.bisect_left(X, L)
  right = bisect.bisect_right(X, R)
  print(people[right] - people[left])


