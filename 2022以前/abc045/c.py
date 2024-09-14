# 1 以上 9 以下の数字のみからなる文字列 
# S が与えられます。 この文字列の中で、あなたはこれら文字と文字の間のうち、いくつかの場所に + を入れることができます。 一つも入れなくてもかまいません。 ただし、+ が連続してはいけません。

# このようにして出来る全ての文字列を数式とみなし、和を計算することができます。

# ありうる全ての数式の値を計算し、その合計を出力してください。

# 125
s = list(map(int, input()))
# print(s)
ans = 0
for i in range(1<<len(s)-1):
    k = False
    num = s[0]
    for j in range(1, len(s)):
        # 00
        # print(i >> j)
        if (i >> (j-1)) & 1 == 0:
            # 00->125
            # 10->1 + 25
            # print( s[j] + (10 * num), '=', s[j], '+', (10 * num))   
            num = s[j] + (10 * num)
        else:
            k = True
            # 1 +
            ans += num
            # print('ans +=', s[j])
            num = s[j]
        
    # print(num)
    ans += num


print(ans)