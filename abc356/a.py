# 正整数 
# N,L,R が与えられます。
# 長さ 
# N の数列 
# A=(1,2,…,N) に対し、 
# L 項目から 
# R 項目までを逆順に並べ替えるという操作を一度行いました。
# 操作後の数列を出力してください。

# 5 2 3

n, l, r = map(int, input().split())
a = []
for i in range(n):
  a.append(i+1)

ans = a[:l-1] + a[l-1:r][::-1] + a[r:]  

print(*ans)
