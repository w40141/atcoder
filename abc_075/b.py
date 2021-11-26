def change_start(s):
    return 0 if s == "." else -9


def change_end(s):
    return str(s) if s >= 0 else "#"


h, w = map(int, input().split())
field_org = [input() for _ in range(h)]
field = (
    [[0 for _ in range(w + 2)]]
    + [[0] + list(map(change_start, line)) + [0] for line in field_org]
    + [[0 for _ in range(w + 2)]]
)


def plus(i, j):
    field[i][j + 1] += 1
    field[i][j - 1] += 1
    field[i + 1][j - 0] += 1
    field[i + 1][j + 1] += 1
    field[i + 1][j - 1] += 1
    field[i - 1][j - 0] += 1
    field[i - 1][j + 1] += 1
    field[i - 1][j - 1] += 1


for i, line in enumerate(field_org):
    for j, point in enumerate(line):
        if point == "#":
            plus(i + 1, j + 1)


for r in field[1:-1]:
    print("".join(map(change_end, r[1:-1])))
