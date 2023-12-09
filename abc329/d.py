from collections import defaultdict
# 3 7
# 1 2 2 3 1 3 3

n, m = map(int, input().split())
v = list(map(int, input().split()))


count = [0] * (m+1)

#当選者
winners = 0
winners_vote = 0
for i in range(m):
    count[v[i]] += 1
    print(count)
    if count[v[i]] > winners_vote:
        winners = v[i]
        winners_vote = count[v[i]]
    elif count[v[i]] == winners_vote:
        winners = min(winners, v[i])
    print(winners)


