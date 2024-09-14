x, y = map(int, input().split(" "))

k = x - y
if -2 <= k and k <= 3:
    print("Yes")
else:
    print("No")