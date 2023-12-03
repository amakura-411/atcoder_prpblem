from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
# 1 4 1 4 2


# タプルを作る（数と順番を入れた）
value_index = defaultdict(list)
for i, num in enumerate(A):
    value_index[num].append(i)
# {1: [0, 2], 4: [1, 3], 2: [4]}

ans = [0] * N
# ans = [0, 0, 0, 0, 0]
sum = 0

# 降順にソートしたタプルを順番に取り出す
for num, index_list in sorted(value_index.items(), reverse=True):
    # 4, [1, 3]
    # 2, [4]
    # 1, [0, 2]
    # 降順にソートしたタプルの中のindex_listを順番に取り出す
    for index in index_list:
        # 1, 3
        # 4
        # 0, 2
        # index_listの中のindex
        ans[index] = sum

    sum = sum + num * len(index_list)

print(*ans)