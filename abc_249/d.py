import numpy as np

n = int(input())
a_li = list(map(int, input().split()))
a_nd = np.array(a_li)
count = 0
for i in range(n):
    tmp_nd = a_nd / a_nd[i]
    for m in a_nd:
        count += sum(tmp_nd == m)
print(count)
