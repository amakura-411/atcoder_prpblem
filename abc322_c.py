# 3 2
# 2 3
# ３日間中２日間花火がある。
# 花火の日程は２行目に与えられる。

days, num = map(int, input().split())
hanabi = list(map(int, input().split()))

# i 日目以降で初めて花火が上がるのは、i 日目から数えて何日後か

count = 0
for day in range(1, days+1):
    if hanabi[count] == day:
        print(0)
        count += 1
    else:
        ans = hanabi[count] - day
        print(ans)
