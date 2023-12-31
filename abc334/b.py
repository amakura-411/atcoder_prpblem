# 東西に無限に伸びる道路があり、この道路上のある基準となる地点から東に 
# xm のところにある地点の座標は 
# x と定められています。 特に、基準となる地点から西に 
# xm のところにある地点の座標は 
# −x です。

# すぬけ君は今から、座標が 
# A である地点を基点にして 
# Mm おきにクリスマスツリーを立てます。 すなわち、座標がある整数 
# k を用いて 
# A+kM と表されるような地点それぞれにクリスマスツリーを立てます。

# 高橋君と青木君はそれぞれ座標が 
# L,R (L≤R) である地点に立っています。 高橋君と青木君の間（高橋君と青木君が立っている地点を含む）に立てられるクリスマスツリーの本数を求めてください。

# 5 3 -1 6
a, m, l, r = map(int, input().split(" "))
ans = 0
# -177018739841739480 2436426 -80154573737296504 585335723211047198

# -80154573737296504 ~ -177018739841739480 ~  585335723211047198
# -1 0 1, 1-> -1 0 1

if l <= a or a <= r:
    # print("aがl~rの間にある場合")
    # aがl~rの間にある場合
    # 5 3 -1 6 -> 5, 2, -1...
    # l~aの個数
    # 切り捨て除算
    ans += (a - l) // m
    # -1, 0, 1, 2, 3, 4, 5まで
    # a~rの個数
    ans += (r - a) // m
    print(ans + 1)

else:
    # aがl~rの間にない場合
    print(0)


# aからlまでの個数
# aからrまでの個数
