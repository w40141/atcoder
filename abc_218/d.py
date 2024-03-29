def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] //= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

x_same_points = {}
for i, point1 in enumerate(points):
    for j, point2 in enumerate(points[i + 1 :]):
        if point1[0] == point2[0]:
            y_list = (
                [point1[1], point2[1]]
                if point1[1] < point2[1]
                else [point2[1], point1[1]]
            )
            y_tuple = tuple(y_list)
            if y_tuple in x_same_points:
                x_same_points[y_tuple] += 1
            else:
                x_same_points[y_tuple] = 1

answer = 0
for value in x_same_points.values():
    if value > 1:
        answer += cmb(value, 2)

print(answer)
