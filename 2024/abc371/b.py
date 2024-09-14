# 長男 = 「太郎」

# N 戸の家があり、 M 人の赤子
# i 番目に生まれた赤子は、Ai番目の家
# B iが M のとき男の子、F のとき女の子です。

N, M = map(int, input().split())

house = [False] * N

for i in range(M):
  a, b = input().split(' ')
  if b == 'F':
    # 女性の時は、すべて'NO'
    print('No')
  else:
    # 男性の場合、house[a] = TRUEであれば'NO'、そうでなければ'YES'
    if house[int(a)-1] == True:
      print('No')
    else:
      house[int(a)-1] = True
      print('Yes')
