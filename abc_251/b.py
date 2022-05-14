import itertools
from typing import Set

n, w = map(int, input().split())
A = sorted(list(map(int, input().split())))

answers: Set[int] = set()
m = 4 if n > 3 else n + 1
for i in range(1, m):
    for p in itertools.combinations(A, i):
        tmp = sum(p)
        if tmp <= w:
            answers.add(tmp)
print(len(answers))
