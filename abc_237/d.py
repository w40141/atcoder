from collections import deque

n = int(input())
s = input()[::-1]
d = deque([n])
for i, si in enumerate(s, 1):
    if si == "L":
        d.append(n - i)
    else:
        d.appendleft(n - i)

print(" ".join(map(str, d)))
