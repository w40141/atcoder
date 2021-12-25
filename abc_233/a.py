x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    z = y - x
    if z % 10 == 0:
        print(z // 10)
    else:
        print(z // 10 + 1)
