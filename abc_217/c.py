n = int(input())
p = list(map(int, input().split()))

q = [0 for _ in range(n)]
for index in range(n):
    q[p[index] - 1] = index + 1

print(*q)
