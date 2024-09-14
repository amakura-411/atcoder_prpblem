
n, m = map(int, input().split(" "))

a = [0 for _ in range(m)]

for i in range(m):
    # kは電球iにつながっているスイッチの数
    # numはそのスイッチの番号
    k, *num = map(int, input().split(" "))
    a[i] = num

# p 2 で割った余りが piに等しい時は点灯する
p = list(map(int, input().split(" ")))

ans = 0
for i in range(1<<n):
    # n = 3とすると
    # iは0から7までの8通りの組み合わせを試す
    on = 0 
    for j in range(m):
        # jは電球の番号
        count = 0
        for s in a[j]:
            # print(i, j, s)
            # 電球[j]のスイッチsのon/offを判定
            # i = 000
            # m = 2
            # s(a[0]) = 1, s(a[1]) = 2
            # j = 0
            if i & (1 << s-1):
                # print("i & (1 << s)", i & (1 << s))
                count += 1

            # 電球はonになっているスイッチがp[i]と等しい場合に点灯する
        if count % 2  == p[j]:
            # print("count % 2  == p[j]", count % 2  == p[j])
            # print('on', on)
            on += 1
        # print("on == m", on, m)
    if on == m:
        ans += 1



print(ans)


