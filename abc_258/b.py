n = int(input())
A = [list(input()) for _ in range(n)]


def route(i, j, A):
    max_num = -(10** 10)
    # up
    max_num = max(max_num, int(''.join([A[(i - k) % n][j] for k in range(n)])))
    # right-up
    max_num = max(max_num, int(''.join([A[(i - k) % n][(j + k) % n] for k in range(n)])))
    # right
    max_num = max(max_num, int(''.join([A[i][(j + k) % n] for k in range(n)])))
    # right-down
    max_num = max(max_num, int(''.join([A[(i + k) % n][(j + k) % n] for k in range(n)])))
    # down
    max_num = max(max_num, int(''.join([A[(i + k) % n][j] for k in range(n)])))
    # left-down
    max_num = max(max_num, int(''.join([A[(i + k) % n][(j - k) % n] for k in range(n)])))
    # left
    max_num = max(max_num, int(''.join([A[i][(j - k) % n] for k in range(n)])))
    # left-up
    max_num = max(max_num, int(''.join([A[(i - k) % n][(j - k) % n] for k in range(n)])))
    return max_num


max_num = -(10** 10)
for i in range(n):
    for j in range(n):
        max_num = max(max_num, route(i, j, A))
print(max_num)
