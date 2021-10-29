a, b, c, x, y = tuple(map(int, input().split()))


min_value = 5000 * 1000000
index = max(x, y)
for i in range(index + 1):
    value = 0
    value += a * max(x - i, 0)
    value += b * max(y - i, 0)
    value += c * 2 * i
    min_value = min(min_value, value)

print(min_value)
