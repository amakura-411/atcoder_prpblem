# 10
# 1937458062
# を１つずつ配列に入れる

m = int(input())
a = input()
b = input()
c = input()

flag =  False

num = 0
ans = 0
limit = m * 3 + 2



def distance(num, count, a, b, t):
    b_f = False
    c_f = False
    seq = 0

    # print('num', num)
    for i in range(t+1, limit):
        s = i%m
        if num == a[s] and (b_f == False):
            # print('seq' , i)
            seq = i
            b_f = True
            if c_f:
                return i
            continue
        if num == b[s] and (c_f == False):
            # print('seq' , i)
            seq = i
            c_f = True
            if b_f:
                return i
            continue
    return count


count = m*3 + 100
for i in range(0, m):
    # print('a')
    count = min(distance(a[i], count, b, c, i), count)
    count = min(distance(a[i], count, c, b, i), count)
    # print('b')
    count = min(distance(b[i], count, a, c, i), count)
    count = min(distance(b[i], count, c, a, i), count)
    # print('c')
    count = min(distance(c[i], count, a, b, i), count)
    count = min(distance(c[i], count, b, a, i), count)

    # print(i , '番目は' ,count)


# print(count)
if count == m*3 + 100:
    print(-1)
else:
    print(count)
    # print(a_sec)










