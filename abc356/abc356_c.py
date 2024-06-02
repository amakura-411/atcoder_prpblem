# N:鍵の数（何本かの鍵は正しい鍵で、それ以外はダミーの鍵）
# ドアX は正しい鍵を K 本以上挿し込んだ時、またその時に限って開きます

# M 回のテスト
# C本の鍵（Ai...)をドアXに挿し込む
# R i= o ならドアXは開く
# R i= x ならドアXは開かない

# テスト結果にも矛盾しない組み合わせの個数

n, m, k = map(int, input().split())


Keys = []
fail = []
success = []
for i in range(m):


  Keys.append(input().split(" "))

# print(Keys)
ans = 0
for i in range(1<<n):
  count = 0
  for j in range(n):
    if (i >> j) & 1:
      count += 1
      keycount = 0
    # 1の数がK以上なら
    if count >= k:
      # テスト結果のチェック
      for key in Keys:
        keyLists = list(key[1:-1])
        if key[-1] == 'o':
          success = 0
          for kl in keyLists:
            if (i >> int(kl)-1) & 1 == 1:
              success += 1
          if success >= k:
            keycount += 1
        else:
          fail = 0
          for kl in keyLists:
            if (i >> int(kl)-1) & 1 == 1:
              fail += 1
              if fail >= k:
                break
          if fail < k:
            keycount += 1
        # print('keyLists', keyLists, 'bin', bin(i), 'key', key, 'keycount', keycount)
      if keycount == m:
        # print('ヨシ')
        ans += 1

# 1 2 3
print(ans)




