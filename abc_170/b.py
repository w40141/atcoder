x, y = map(int, input().split())

i = 4 * x - y
j = y - 2 * x

if i >= 0 and j >= 0 and i % 2 == 0 and j % 2 == 0:
    pass
    print("Yes")
else:
    print("No")
