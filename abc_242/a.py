a, b, c, x = map(int, input().split())

if x <= a:
    print(float(1))
elif x <= b:
    print(c / (b - a))
else:
    print(float(0))
