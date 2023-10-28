n, m, p =map(int, input().split(" "))

count = 1
day = m
while day <= n:
    count += 1
    day += p
print(count-1)