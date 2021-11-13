n, k, a = map(int, input().split())

k += a - 1
m = k % n
if m == 0:
    print(n)
else:
    print(m)
