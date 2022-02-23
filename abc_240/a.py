a, b = map(int, input().split())
if b - a == 1:
    print('Yes')
else:
    if b == 10 and a == 1:
        print('Yes')
    else:
        print('No')
