N, t = input().split(" ")
n = int(N)
def sameT(s, t):
    if s == t:
        return True
    t_length = len(t)
    s_length = len(s)
    new_s = ""

    if s_length == t_length:
        # T のある 1 文字を別の英小文字に変更して得られる文字列 
        for i in range(s_length):
            if s[i] != t[i]:
                new_s = s[:i] + t[i] + s[i+1:]
                break
    elif s_length > t_length:
        # T のいずれか 1 つの位置（先頭と末尾も含む）に英小文字を 1 つ挿入して得られる文字列 →sの方が多い。
        for i in range(t_length):
            if s[i] != t[i]:
                new_s = s[:i] + s[i+1:]
                break
        if new_s == "":
            new_s = s[:-1]
            # print(new_s)
    elif s_length < t_length:
        # T のいずれか 1 つの位置（先頭と末尾も含む）に英小文字を 1 つ削除して得られる文字列 →sの方が少ない。
        for i in range(s_length):
            if s[i] != t[i]:
                new_s = s[:i] + t[i] + s[i:]
                break
        if new_s == "":
            new_s = s + t[-1]
    else:
        return False
    if new_s == t:
        return True
    else:
        return False
    
ans = []
for i in range(n):
    s = input()
    if sameT(s, t):
        ans.append(i+1)

print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=" ")
