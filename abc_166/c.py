raw_input = list(map(int, input().split()))
n = raw_input[0]
m = raw_input[1]
h = list(map(int, input().split()))
loads = {i+1: [] for i in range(n)}
for _ in range(m):
    raw_input = list(map(int, input().split()))
    a = raw_input[0]
    b = raw_input[1]
    loads[a].append(h[b-1])
    loads[b].append(h[a-1])
# print(loads)
counter = 0
for k, v in loads.items():
    if len(v) == 0:
        counter += 1
    elif max(v) < h[k-1]:
        counter += 1
print(counter)
