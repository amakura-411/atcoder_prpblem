n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
# ソート
C.sort()

num = m + n 
for i in range(num-1):
  if C[i] in A and C[i+1] in A:
    print('Yes')
    exit()
print('No')
