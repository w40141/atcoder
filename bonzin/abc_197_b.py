h, w, x, y = map(int, input().split())
field = [list(input()) for _ in range(h)]

count = 0
x = x - 1
y = y - 1
for i in range(x + 1, h):
    if field[i][y] == ".":
        count += 1
    else:
        break
for i in range(x - 1, -1, -1):
    if field[i][y] == ".":
        count += 1
    else:
        break
for i in range(y + 1, w):
    if field[x][i] == ".":
        count += 1
    else:
        break
for i in range(y - 1, -1, -1):
    if field[x][i] == ".":
        count += 1
    else:
        break
if field[x][y] == ".":
    count += 1
print(count)
