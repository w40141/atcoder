import numpy as np


n = int(input().strip())
a = np.array(list(map(int, input().split())))
count = 0
sub_a = np.array([[j - i for j in range(n)] for i in range(n-1)])
add_a = np.array([[a_h + a[i] for a_h in a] for i in range(n-1)])
for i in range(n-1):
    cal_a = sub_a[i] - add_a[i]
    count += np.count_nonzero(cal_a == 0)
print(count)
