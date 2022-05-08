h, w = map(int, input().split())
r, c = map(int, input().split())

count = 0
if 1 <= r - 1 <= h:
    count += 1
if 1 <= r + 1 <= h:
    count += 1
if 1 <= c - 1 <= w:
    count += 1
if 1 <= c + 1 <= w:
    count += 1
print(count)
