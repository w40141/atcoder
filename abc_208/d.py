tmp = list(map(int, input().split()))
n = tmp[0]
m = tmp[1]

route = dict()
for _ in range(m):
    tmp = list(map(int, input().split()))
    a = tmp[0]
    b = tmp[1]
    c = tmp[2]
    route[(a, b)] = c
