# 百の位の数と十の位の数の積が一の位の数と等しいもの
num = int(input())

while(True):
    #１桁ずつに分解
    h = num // 100
    j = num // 10 % 10
    i = num % 10
    if h * j == i:
        print(num)
        break
    num += 1
    
