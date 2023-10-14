#  N=2^x3^yが成り立つとき、Yesを出力する。

def two(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count

def three(n):
    count = 0
    while n % 3 == 0:
        n = n / 3
        count += 1
    return count


n = int(input())
two_count = two(n)
three_count = three(n)
if 2**two_count * 3**three_count == n:
    print("Yes")
else:
    print("No")

