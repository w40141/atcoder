n, q = map(int, input().split())
d = list(input())
start = 0
for _ in range(q):
    t, s = map(int, input().split())
    if t == 1:
        start = (start - s) % n
    else:
        print(d[(start + s - 1) % n])
