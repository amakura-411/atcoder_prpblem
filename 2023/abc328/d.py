# BAABCBCCABCAC
# 0122211011100
s = input()
stash = []
for i in range(len(s)):
    stash.append(s[i])
    if len(stash) >= 3:
        if stash[-3] == 'A' and stash[-2] == 'B' and stash[-1] == 'C':
            stash.pop()
            stash.pop()
            stash.pop()
print(*stash, sep='')