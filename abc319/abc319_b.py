# 正整数 N が与えられるので、下記で定まる長さ (N+1) の文字列 s0 s1…s Nを出力してください。
# 1 以上 9 以下の N の約数 j であって、i が N/j の倍数であるものが存在するとき、
# そのような j のうち最小のものに対応する数字を s iとする。（よって、この場合 siは 1 、2 、… 、9 のいずれか）
# j が存在しないとき、s iは - 
def divisor(i, n):
    if i == 0:
        return '1'
    for j in range(1, 10):
        if n % j == 0 and i % (n // j) == 0:
            return str(j)
    return '-'

N = int(input())

ans = ""

for i in range(N+1):
    ans += divisor(i, N)

print(ans)

# ここまではわかる
