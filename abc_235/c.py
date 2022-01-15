from typing import Dict, List


n, q = map(int, input().split())
a = map(int, input().split())
query = [map(int, input().split()) for _ in range(q)]

numbers: Dict[int, List[int]] = dict()
for i, ai in enumerate(a):
    numbers.setdefault(ai, [])
    numbers[ai].append(i+1)

for qu in query:
    x, k = qu
    if x in numbers:
        xi = numbers[x]
        if len(xi) >= k:
            print(xi[k-1])
        else:
            print(-1)
    else:
        print(-1)
