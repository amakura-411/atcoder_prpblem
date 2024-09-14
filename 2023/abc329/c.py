
n = int(input())
s = input()

f = s[0]
ans = 0

count = [0] * 26

num = 0
for i in range(0, n):
    # f == s[i]のとき
    # print(f, s[i], count[ord(f) - ord("a")], num + 1)
    if f == s[i]:
        num += 1
        count[ord(f) - ord("a")] = max(count[ord(f) - ord("a")], num)
    else:
        # f != s[i]のとき
        num = 1
        count[ord(s[i]) - ord("a")] = max(count[ord(s[i]) - ord("a")], 1)
        f = s[i]
    # print(count[ord(f) - ord("a")])



ans = 0
# print(count)
for i in range(26):
    ans += count[i]

print(max(1, ans))

