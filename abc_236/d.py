from typing import List, Tuple


n = int(input())
aisho = [
    [0 for _ in range(i + 1)] + list(map(int, input().split())) for i in range(2 * n)
]


def f(x):
    if x == 1:
        return 1
    else:
        return (2 * -1) * f(x - 1)


def pairs(x: List[int], i: int) -> List[Tuple[int, int]]:
    if len(x) == 2:
        return [tuple(x)]
    else:
        return [tuple([x[0], x[i]])] + pairs(x[1:i] + x[i + 1 :], 1)


hito = list(range(2 * n))
print(pairs(hito, 1))
