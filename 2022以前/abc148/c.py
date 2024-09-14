# n = 人数
n = int(input()) 
speaks = []

for i in range(n):
    speak = []
    s = int(input())
    for j in range(s):
        # x番目の人はyが１なら正直であるといい、０なら不親切であるという
        x, y = map(int, input().split(" "))
        speak.append((x, y))
    speaks.append(speak)
# print(speaks)
ans = 0
count = 0
for i in range(1<<n):
    # iは正直者の組み合わせ
    for j in range(n):
        if (i >> j) & 1 == 0: 
            continue
        for x, y in speaks[j]:
            if y != (i >> x-1) & 1:
                break
        else:
            continue
        break
    else:
        ans = max(ans, i.bit_count())

            # if s[k][1] != (i >> s[k][0]) & 1:
            #     break


print(ans)

