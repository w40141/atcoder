n, x = map(int, input().split())
d = 1
for _ in range(n):
    a, b = map(int, input().split())
    d = (d << a) | (d << b)
if (d >> x) & 1 == 1:
    print('Yes')
else:
    print('No')
