n = int(input())
str = input()
count = 0
ans = -1
for i in range(n-2):
    if str[i] == 'A' and str[i+1] == 'B' and str[i+2] == 'C':
        ans = i
        break
print(ans)
