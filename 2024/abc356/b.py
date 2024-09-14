n, m = map(int, input().split())

# mは種類、
# i番目は１日にAi以上必須
# N 品摂取し、、i 品目の食品からは栄養素 j を X i,j
# M 種類全ての栄養素で目標を達成しているかどうか

A = list(map(int, input().split()))
X = [ list(map(int, input().split())) for _ in range(n)]
# print(A)
# print(X)


status = [0] * m

for i in range(n):
  for j in range(m):
    status[j] += X[i][j]

# print(status)

for i in range(m):
  # print(status[i], A[i])
  if status[i] < A[i]:
    print('No')
    exit()
print('Yes')