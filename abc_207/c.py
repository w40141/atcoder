from typing import Set


n = int(input())


def make_range(t, left, right):
    if t == 1:
        return set(range(left, right + 1))
    elif t == 2:
        return set(range(left, right))
    elif t == 3:
        return set(range(left + 1, right + 1))
    else:
        return set(range(left + 1, right))


ans: Set = set([])
input_range = []
for i in range(n):
    tmp = list(map(int, input().split()))
    t = tmp[0]
    left = tmp[1]
    right = tmp[2]
    input_range.append((t, left, right))

for i, t_i in enumerate(input_range):
    for j, t_j in enumerate(input_range[i + 1:]):
    pass
    ans_tmp = make_range(t, left, right)
    print(ans_tmp)
    print(ans)
    if not ans:
        ans = ans_tmp
    else:
        ans &= ans_tmp
print(ans)
