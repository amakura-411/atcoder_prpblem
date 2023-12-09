


## C - Count xxx

## 問題

英小文字からなる長さ N の文字列 S が与えられます。

S の空でない部分文字列であって、1 種類の文字のみからなるものの数を求めてください。 ただし、文字列として等しい部分文字列同士は、取り出し方が異なっても区別しません。

なお、S の空でない部分文字列とは、S の先頭から 0 文字以上、末尾から 0 文字以上削除して得られる文字列のうち、長さが 1 以上であるもののことをいいます。 例えば、ab や abc は abc の空でない部分文字列ですが、ac や空文字列は abc の空でない部分文字列ではありません。

### コード

```python

n = int(input())
s = input()

f = s[0]
count = [0] * 26
ans = 0
num = 0

for i in range(0, n):
    if f == s[i]:
        num += 1
        count[ord(f) - ord("a")] = max(count[ord(f) - ord("a")], num)
    else:
        num = 1
        count[ord(s[i]) - ord("a")] = max(count[ord(s[i]) - ord("a")], 1)
        f = s[i]

ans = 0
# print(count)
for i in range(26):
    ans += count[i]

print(max(1, ans))

```

###　解説

この問題は、それぞれの文字について、連続する文字数を数え、それを足し合わせることで解くことができる。

1.標準入力

```python
n = int(input())
s = input()
```

2.初期化

```python
# 最初の文字をfに代入
f = s[0]
# アルファベットの数を数えるための配列
count = [0] * 26
ans = 0 # 回答用の変数
num = 0 # 連続する文字数を数えるための変数
```

3.文字列を走査

```python
# iからnまで走査
for i in range(0, n):
    if f == s[i]:
        # 同じ文字が続いている場合
        # numを1増やす
        num += 1
        #ついでに、countも更新
        # ord()で文字を数値に変換し、aを引くことで、aを0としたアルファベットの順番に変換
        count[ord(f) - ord("a")] = max(count[ord(f) - ord("a")], num)
    else:
        # 違う文字が出てきた場合
        # numを1に戻す
        num = 1
        # ついでに、countも更新
        # ord()で文字を数値に変換し、aを引くことで、aを0としたアルファベットの順番に変換
        count[ord(s[i]) - ord("a")] = max(count[ord(s[i]) - ord("a")], 1)
        # fに新しい文字を代入
        f = s[i]
```

3.回答

```python

for i in range(26):
    # アルファベットの数を足し合わせる
    ans += count[i]

# 1文字だけの場合は、答えは1なので、max関数を使って、ansと1の大きい方を出力
print(max(1, ans))

```


