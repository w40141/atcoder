a, b, k = map(int, input().split())


def calc(a, k, i):
    return a * k ** i


i = 0
while True:
    ans = calc(a, k, i)
    if b > ans:
        i += 1
    else:
        break
print(i)
