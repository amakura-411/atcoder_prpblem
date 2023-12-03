N, Q = map(int, input().split())
mass = [input() for _ in range(N)]

#累積和
num = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        num[i][j] += 1 if mass[i-1][j-1] == "B" else 0
        num[i][j] += num[i-1][j]
        num[i][j] += num[i][j-1]
        num[i][j] -= num[i-1][j-1]

def counterBlack(H, W):
    if H <=N and W <= N:
        # 範囲内の状態ならそのまま返す
        return num[H][W]
    # HをNで割った商と余り
    hq, hr = divmod(H, N)
    # WをNで割った商と余り
    wq, wr = divmod(W, N)
    ret = 0
    # massの中範囲の黒の数 * Nで割った商
    ret += counterBlack(N, N) * hq * wq
    # massの中範囲の黒の数 * 余り
    ret += counterBlack(hr, N) * wq
    # massの中範囲の黒の数 * 余り
    ret += counterBlack(N, wr) * hq
    # massの中範囲の黒の数
    ret += counterBlack(hr, wr)
    return ret

# 与えられた4つの座標に対応する領域内に存在する'B'の数を計算します
def checkerBlock(A, B, C, D):
# f(A,B,C,D)
# =((d)に含まれる黒マスの個数)
# =((a),(b),(c),(d)に含まれる黒マスの個数)
# −((a),(b)に含まれる黒マスの個数)
# −((a),(c)に含まれる黒マスの個数)
# +((a)に含まれる黒マスの個数)
# =f(0,0,C,D)−f(0,0,C,B)−f(0,0,A,D)+f(0,0,A,B)

    return counterBlack(C, D) - counterBlack(A, D) - counterBlack(C, B) + counterBlack(A, B)

    

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(checkerBlock(a, b, c + 1, d + 1))





