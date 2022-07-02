k = int(input())
h = str(21 + (k // 60))
m = k % 60
ms = str(m) if m >= 10 else '0' + str(m)
print(h + ':' + ms)
