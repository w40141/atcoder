l1, r1, l2, r2 = map(int, input().split())
tmp = min(r1, r2) - max(l1, l2)
if tmp < 0:
    print(0)
else:
    print(tmp)
