a, b, c, d, e, f, x = map(int, input().split())


def calc(a, b, c, x):
    t = 0
    while True:
        if x >= a:
            t += a * b
            x -= a
        else:
            t += x * b
            break
        if x >= c:
            x -= c
        else:
            break
    return t


t_m = calc(a, b, c, x)
a_m = calc(d, e, f, x)
if t_m == a_m:
    print("Draw")
elif t_m > a_m:
    print("Takahashi")
else:
    print("Aoki")
