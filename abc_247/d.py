from collections import deque

Q = int(input())
d = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append((query[1], query[2]))
    else:
        c = query[1]
        ans = 0
        while True:
            number, count = d.popleft()
            count_tmp = count - c
            if count_tmp > 0:
                print(ans + number * c)
                d.appendleft((number, count_tmp))
                break
            elif count_tmp == 0:
                print(ans + number * c)
                break
            else:
                ans += number * count
                c = - count_tmp
