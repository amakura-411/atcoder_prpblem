#  > > >
ab, ac, bc = input().split(' ')

a = 0
b = 0
c = 0


if ab == '<':
  b += 1
else:
  a += 1

if ac == '<':
  c += 1
else:
  a += 1

if bc == '<':
  c += 1
else:
  b += 1

if a == 1:
  print('A')
elif b == 1:
  print('B')
else:
  print('C')

