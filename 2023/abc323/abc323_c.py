n, m = map(int, input().split(" ")) # n:人数 m:問題数

points = list(map(int, input().split(" ")))
# print(points)
num_point = dict() # number:point
user_point = dict() # number:point
max_point = -1
user_not_point =[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    point = i
    problem = input()
    for j in range(m):
        if problem[j] == "o":
            point += points[j]
        elif problem[j] == "x":
            user_not_point[i][j] = points[j]
    if max_point < point:
        max_point = point
    user_point[i+1] = point

for i in range(n):
    count = 0
    if user_point[i+1] < max_point:
        # 小さい時に
        user_problem = sorted(user_not_point[i], reverse=True)
        point = max_point - user_point[i+1]
        for j in range(len(user_problem)):
            if point <= 0:
                break
            # print(point, max_point)
            point -= user_problem[j]
            count += 1
    print(count)



