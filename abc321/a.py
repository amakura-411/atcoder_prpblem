n = input()


num = int(n[0])
ans = "Yes"
for i in range(1, len(n)):
    # print(num, n[i])
    if int(n[i]) > num:
        ans = "No"
        break
    num = int(n[i])
print(ans)