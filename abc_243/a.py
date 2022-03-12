v, a, b, c = map(int, input().split())

s = a + b + c
v %= s
v -= a
if v < 0:
    print("F")
else:
    v -= b
    if v < 0:
        print("M")
    else:
        v -= c
        if v < 0:
            print("T")
