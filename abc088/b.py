# 2
# 3 1

n = int(input())
card = list(map(int, input().split(" ")))
# sort
card.sort(reverse=True)
ans = sum(card[::2]) - sum(card[1::2])
print(ans)