tmp = list(map(int, input().split()))
a = tmp[0]
b = tmp[1]
c = tmp[2]

if c % 2 == 0:
    if abs(a) == abs(b):
        print('=')
    elif abs(a) < abs(b):
        print('<')
    else:
        print('>')
else:
    if a == b:
        print('=')
    elif a < b:
        print('<')
    else:
        print('>')
