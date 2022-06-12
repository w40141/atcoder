x, a, d, n = map(int, input().split())
z = a + d * (n - 1)
min_n = min(a, z)
max_n = max(a, z)
if x < min_n:
    print(min_n - x)
elif x > max_n:
    print(x - max_n)
elif min_n < x < max_n:
    abs_d = abs(d)
    t = (x - a) % abs_d
    print(min(abs_d - t, t))
else:
    print(0)
