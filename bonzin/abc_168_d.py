from typing import List, Deque
from collections import deque

n, m = map(int, input().split())
connect: List[List[int]] = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

que: Deque[int] = deque([1])
visited: List[bool] = [False] * (n + 1)
distance: List[int] = [0] * (n + 1)

visited[1] = True
while len(que) > 0:
    now = que.popleft()
    for next in connect[now]:
        if visited[next]:
            continue
        visited[next] = True
        distance[next] = now
        que.append(next)

print('Yes')
for i in distance[2:]:
    print(i)
