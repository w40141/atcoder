n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

lis = [0 for _ in range(n)]
for edge in edges:
    x = edge[0] - 1
    y = edge[1] - 1
    lis[x] += 1
    lis[y] += 1

for li in lis:
    if li == n - 1:
        print("Yes")
        break
else:
    print("No")
