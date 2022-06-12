import math

n, k = map(int, input().split())
A = list(map(int, input().split()))
people = [tuple(map(int, input().split())) for _ in range(n)]
length = -(10 ** 20)
for i in range(n):
    tmp_len = 10 ** 20
    for j in A:
        k = j - 1
        if i == k:
            pass
        x1 = people[i][0]
        y1 = people[i][1]
        x2 = people[k][0]
        y2 = people[k][1]
        tmp = (x1 - x2) ** 2 + (y1 - y2) ** 2
        tmp_len = min(tmp, tmp_len)
    length = max(length, tmp_len)
print(math.sqrt(length))
