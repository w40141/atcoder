from typing import List
from collections import deque

n, m = map(int, input().split())
loads: List[List[int]] = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    loads[a].append(b)


def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    count = 1
    que = deque()
    que.append(start)
    while len(que) > 0:
        now_city = que.popleft()
        for to_city in loads[now_city]:
            if not visited[to_city]:
                visited[to_city] = True
                count += 1
                que.append(to_city)
    return count


ans = 0
for i in range(1, n + 1):
    ans += bfs(i)
print(ans)
