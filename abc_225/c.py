import numpy as np

n, m = map(int, input().split())
matrix = np.array([list(map(int, input().split())) for _ in range(n)])


def sub(a, b, x):
    return b - a == x


def check_index(li):
    for i in range(m - 1):
        if not sub(li[i], li[i + 1], 1):
            return False
    return True


def check_column(li):
    for i in range(n - 1):
        if not sub(li[i], li[i + 1], 7):
            return False
    return True


def check_edge(matrix):
    li = matrix[0]
    start = li[0]
    end = li[-1]
    x = start % 7
    y = end % 7
    if y == 0 or y >= x or 7 >= len(li):
        return True
    else:
        return False


def check_matrix(matrix):
    for li in matrix:
        if not check_index(li):
            return False

    for li in matrix.T:
        if not check_column(li):
            return False

    return check_edge(matrix)


if check_matrix(matrix):
    print("Yes")
else:
    print("No")
