# あなたは、
# 500 円玉を 
# A 枚、
# 100 円玉を 
# B 枚、
# 50 円玉を 
# C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど 
# X 円にする方法は何通りありますか。

# 同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(a+1):
    for j in range(b+1):
        price = x - (500 * i + 100 * j)
        if price < 0:
            break
        if price % 50 == 0 and price / 50 <= c:
            # print(i, j, price / 50)
            # print(i*500,j*100, price, (i*500 + j*100 + price) )
            ans += 1


print(ans)
