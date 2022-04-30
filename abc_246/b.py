import math

x, y = map(int, input().split())

z = x * x + y * y
zn = math.sqrt(z)
print(x/zn, y/zn)
