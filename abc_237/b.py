h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]
for wi in range(w):
    b = [str(a[hi][wi]) for hi in range(h)]
    print(" ".join(b))
