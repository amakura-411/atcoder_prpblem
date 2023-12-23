k = int(input())

count = 0

a = set()
# bit全探索
for s in range(1<<10):
    # print(s)
    count = 0
    for i in range(9, -1, -1):
        print(s>>i, s, i, (s>>i)&1)
        if (s>>i)&1:
            # print(i)
            count = count * 10 + i
            # print(count)
        if count == 0:
            continue    
        a.add(count)

# print(sorted(a))
print(sorted(a)[k-1])
