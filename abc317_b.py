n = int(input())
a = list(map(int, input().split())) 
a.sort()
b = a[0]
for i in range(n):
    if b == a[i]:
        b += 1
        continue
    else:
        print(b)
        break


