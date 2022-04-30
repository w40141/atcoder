from typing import List

n = int(input())

ans: List[int] = []
i = 1
while i * i <= n:
    if n % i == 0:
        ans.append(i)
        if i != n // i:
            ans.append(n // i)
    i += 1
ans.sort()
result: List[str] = [str(a) for a in ans]
print("\n".join(result))
