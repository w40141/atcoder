tmp = list(map(int, input().split()))
a = tmp[0]
b = tmp[1]

if a * 6 >= b and b >= a:
    print('Yes')
else:
    print('No')
