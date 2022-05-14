from typing import Dict, Tuple


n = int(input())
d: Dict[str, int] = {}
award: Tuple[int, int] = (10 ** 6, -10 ** 6)
for i in range(1, n + 1):
    s, t = input().split()
    point = int(t)
    if s in d:
        pass
    else:
        d[s] = point
        if point > award[1]:
            award = (i, point)
print(award[0])
