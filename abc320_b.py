# 文字列 S が与えられます。 
# S の連続する部分文字列のうち、回文であるものの長さの最大値を求めてください。
# ただし、S の連続する部分文字列であって回文であるものは常に存在します。

# TOYOTA
s = input()
n = len(s)
ans = 0
for i in range(n):
    for j in range(i, n):
        t = s[i:j+1]
        if t == t[::-1]:
            ans = max(ans, len(t))
print(ans)
