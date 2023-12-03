m, d = map(int, input().split(" "))

yyyy, mm, dd = map(int, input().split(" "))

dd += 1
if dd > d:
    dd = 1
    mm += 1
if mm > m:
    mm = 1
    yyyy += 1
print(yyyy, mm, dd)