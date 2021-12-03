a, b, c = map(int, input().split())

if a == b == c and a % 2 == 0:
    print(-1)


def exchange(a, b, c):
    h_a = a / 2
    h_b = b / 2
    h_c = c / 2
    return h_b + h_c, h_a + h_c, h_a + h_b


count = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    a, b, c = exchange(a, b, c)
    count += 1

print(count)
