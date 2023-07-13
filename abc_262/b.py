n, m = map(int, input().split())
edges = {i + 1: [] for i in range(n)}
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

count = 0
for first, first_next in edges.items():
    for second in first_next:
        for third in edges[second]:
            if first == third:
                continue
            for fourth in edges[third]:
                if second == fourth:
                    continue
                if first == fourth:
                    count+= 1
                    break

print(count // 6)
