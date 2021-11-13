N = int(input())
S = map(int, input().split())


area = [
    [
        4 * a * b + 3 * a + 3 * b
        for a in range(1, 144)
        if 1000 >= 4 * a * b + 3 * a + 3 * b
    ]
    for b in range(1, 144)
]
p = 0
for s in S:
    for a in area:
        if s in a:
            p += 1
            break

print(N - p)
