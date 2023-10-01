
# S が T の接頭辞であり、かつ接尾辞でもある場合は 0 を、
# S が T の接頭辞であるが、接尾辞でない場合は 1 を、
# S が T の接尾辞であるが、接頭辞でない場合は 2 を、
# S が T の接頭辞でも接尾辞でもない場合は 3 を出力してください。

s_num, t_num = map(int, input().split())
s = input()
t = input()

# S が T の接頭辞 = mathc?(/^S/)

if t.startswith(s) and t.endswith(s):
    print(0)
elif t.startswith(s):
    print(1)
elif t.endswith(s):
    print(2)
else:
    print(3)






