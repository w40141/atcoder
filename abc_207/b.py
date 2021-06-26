import math

tmp = list(map(int, input().split()))
a = tmp[0]
b = tmp[1]
c = tmp[2]
d = tmp[3]

if b == d * c:
    print(-1)
else:
    n = a / (d * c - b)
    if n <= 0:
        print(-1)
    else:
        print(math.ceil(n))
