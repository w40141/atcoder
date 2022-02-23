from typing import List


n = int(input())
a_li = list(map(int, input().split()))
count = 0
now: List[List[int]] = []
for a in a_li:
    count += 1
    if len(now) == 0 or now[-1][0] != a:
        now.append([a, 1])
    else:
        now[-1][1] += 1
        if now[-1][1] == a:
            count -= a
            now = now[: -1]
    print(count)
