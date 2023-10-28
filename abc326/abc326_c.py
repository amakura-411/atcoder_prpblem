#N個のアイテムがあります。
# このアイテムは数直線上にあり、武は 半開区間[x, x+m)の範囲にあるものを取得します

# この時の最大個数を求めよ
n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
a.sort()
a.append(9000000000000)
ans = 0
f = 0
for i in range(n):
    while a[f] < a[i] + m:
        f += 1
    ans = max(ans, f - i)
print(ans)


