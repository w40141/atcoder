import numpy as np


q = int(input())

nums = []
data = np.array([])
for _ in range(q):
    query = list(map(int, input().split()))
    ans = -1
    if query[0] == 1:
        nums.append(query[1])
        data = np.array(nums)
        data.sort()
    elif query[0] == 2:
        x = query[1]
        k = query[2]
        np_d = np.array(data)
        tmp = np_d[np_d <= x]
        try:
            ans = tmp[-k]
        except:
            ans = -1
        print(ans)
    else:
        x = query[1]
        k = query[2]
        np_d = np.array(data)
        tmp = np_d[np_d >= x]
        tmp.sort()
        try:
            ans = tmp[k - 1]
        except:
            ans = -1
        print(ans)
