# 5 4 7
# 3 1 4 9 7

N, L, R = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

#  L < a[i] < R
# |X -a[i]| < |Y - a[i]|
for i in range(N):
    if L <= a[i] <= R:
        print(a[i], end=" ")
    elif a[i] < L:
        print(L, end=" ")
    else:
        print(R, end=" ")
