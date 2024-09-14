S = input()

ans = True
for i in range(1, 16, 2):
    if S[i] =="1":
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")