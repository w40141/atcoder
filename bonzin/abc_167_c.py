n, m, x = map(int, input().split())
C = []
A = []
for _ in range(n):
    b = list(map(int, input().split()))
    C.append(b[0])
    A.append(b[1:])
ans = 10 ** 15

for i in range(1 << n):
    cost = 0
    skill = [0 for _ in range(m)]
    for shift in range(n):
        if i >> shift & 1:
            cost += C[shift]
            for j in range(m):
                skill[j] += A[shift][j]
    if x <= min(skill):
        ans = min(ans, cost)
if ans == 10 ** 15:
    print(-1)
else:
    print(ans)
