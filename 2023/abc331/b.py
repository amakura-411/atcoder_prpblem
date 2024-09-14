import math
N,S,M,L = map(int,input().split(" "))

min_amount = 10**4
price = 10**4
for i in range(N+1):
    # ６個の卵をi個買う
    for j in range(N+1):
        # ８個の卵をj個買う
        price = S*i + M*j
        eggs = N - (i * 6 + j * 8)
        if eggs < 0:
            min_amount = min(min_amount, price)
            continue
        # 12個の卵をeggs個以上になるように買う
        k = math.ceil(eggs / 12)
        price += L * k

        min_amount = min(min_amount, price)     
print(min_amount)




