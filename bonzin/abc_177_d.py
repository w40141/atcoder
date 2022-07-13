from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.n: int = n
        self.parent_size: List[int] = [-1] * n

    def merge(self, a: int, b: int) -> None:
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a: int, b: int) -> bool:
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a: int) -> int:
        return abs(self.parent_size[self.leader(a)])

    def groups(self) -> List[List[int]]:
        result = [[]for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

n, m = map(int, input().split())
uni = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uni.merge(a, b)

friend_size = [len(fri) for fri in uni.groups()]
print(max(friend_size))
