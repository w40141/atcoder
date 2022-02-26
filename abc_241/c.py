import numpy as np

n = int(input())

def tmp(s):
    return 0 if s == "." else 1

def check(li):
    return True

ground = np.array([list(map(tmp, input())) for _ in range(n)])
flag = False
for g in ground:
    if sum(g) >= 6:
        flag |= check(g)
    else:
        pass

ground_T = ground.T
for g in ground:
    if sum(g) >= 6:
        flag |= check(g)
    else:
        pass

g = [ground[i][i] for i in range(n)]
flag |= check(g)

g = [ground[-i -1][i] for i in range(n)]
flag |= check(g)

if flag:
    print("Yes")
else:
    print("No")
