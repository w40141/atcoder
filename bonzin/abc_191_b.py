n, x = map(int, input().split())
a = list(map(int, input().split()))
b = []
for ai in a:
    if ai == x:
        pass
    else:
        b.append(str(ai))
print(" ".join(b))
