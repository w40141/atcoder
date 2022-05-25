from typing import List


n, k = map(int, input().split())
r, s, p = map(int, input().split())
items = list(input())
win = {'r': 'p', 's': 'r', 'p': 's'}
points = {'r': r, 's': s, 'p': p}
hands: List[str] = []
point = 0

for t in items:
    now = win[t]
    if len(hands) >= k:
        if now == hands[-k]:
            now = 'x'
    if now == win[t]:
        point += points[now]
    hands.append(now)
print(point)
