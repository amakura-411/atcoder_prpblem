from collections import defaultdict
# 入力を受け取る部分
N = int(input())
A = list(map(int, input().split()))
#value_index = [(A[1], 1), (A[2], 2), ..., (A[N], N)]
value_index = defaultdict(list)
for i, a in enumerate(A):
    value_index[a].append(i)


sum = 0
ans = [0] * N

for v, i_list in sorted(value_index.items())[::-1]:
    for i in i_list:
        ans[i] = sum
    sum += v*len(i_list)
    
print(*ans)