# 文字列
# S が与えられます。
# S の連続する部分文字列のうち、回文であるものの長さの最大値を求めてください。
# ただし、
# S の連続する部分文字列であって回文であるものは常に存在します。

s = input()

max_num = 0
for i in range(len(s)):
    for j in range(len(s), i, -1):
        if s[i:j] == s[i:j][::-1]:
            max_num = max(max_num, j-i)


print(max_num)
