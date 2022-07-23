a, b, x = map(int, input().split())


def price(a, b, n):
    return a * n + b * int(len(str(n)))


if x < price(a, b, 1):
    print(0)
    exit()

left = 1
right = 10**20

while right - left > 1:
    center = (left + right) // 2
    if price(a, b, center) <= x:
        left = center
    else:
        right = center

if left > 10**9:
    left = 10**9

print(left)
