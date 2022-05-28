from typing import List, Tuple


h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]

os: List[Tuple[int, int]] = []
for i, row in enumerate(field):
    for j, cell in enumerate(row):
        if cell == 'o':
            os.append((i, j))
x = abs(os[0][0] - os[1][0])
y = abs(os[0][1] - os[1][1])
print(x + y)
