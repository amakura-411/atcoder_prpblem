# N=マスの数, Q=クエリの数
N, Q = map(int, input().split())

mass = [input() for _ in range(N)]


# print(mass)
# 累積和
value_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        value_sum[i][j] = value_sum[i-1][j] + value_sum[i][j-1] - value_sum[i-1][j-1]
        value_sum[i][j] = value_sum[i][j] + 1 if mass[i-1][j-1] == "B" else value_sum[i][j]


# 3. 領域内の'B'の数を求める関数
def black_sum(H, W):
    if H <= N and W <= N:
        # 範囲内ならそのまま返す
        return value_sum[H][W]
    
    # 縦横の商と余りを求める
    Hq, Hr = divmod(H, N)
    Wq, Wr = divmod(W, N)
    # retは戻り値を格納する変数
    ret = 0
    # (0, 0) -> (N, N)の領域内の'B'の数
    ret +=black_sum(N, N) * (Hq * Wq)
    # (0, 0) -> (N, Wr)の領域内の'B'の数
    ret +=black_sum(N, Wr) * Hq
    # (0, 0) -> (Hr, N)の領域内の'B'の数
    ret +=black_sum(Hr, N) * Wq
    # (0, 0) -> (Hr, Wr)の領域内の'B'の数
    ret +=black_sum(Hr, Wr)
    return ret


def CountBlack(a, b, c, d):
    # bs(4,5) - bs(0,5) - bs(4,2) + bs(0,2)
    # = bs(c+1, d+1) - bs(a, d+1) - bs(c+1, b) + bs(a, b)
    # = bs(c, d) - bs(a, d) - bs(c, b) + bs(a, b
    return black_sum(c, d) - black_sum(a, d) - black_sum(c, b) + black_sum(a, b)    


for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(CountBlack(a, b, c+1, d+1))