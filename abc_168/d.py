def check(room_checked):
    for i in room_checked:
        if not i:
            return True
    return False


raw_input = list(map(int, input().strip().split()))
n = raw_input[0]
m = raw_input[1]
lines = {i: [] for i in range(m)}
for i in range(m):
    line = list(map(int, input().strip().split()))
    a = line[0] - 1
    b = line[1] - 1
    lines[a].append(b)
    lines[b].append(a)
is_checked_room = [False for _ in range(n)]
sign = [0 for _ in range(n)]
queue = [0]
while check(is_checked_room):
    target = queue[0]
    queue.pop(0)
    is_checked_room[target] = True
    line = lines[target]
    for l in line:
        if not is_checked_room[l]:
            is_checked_room[l] = True
            sign[l] = target
            queue.append(l)
    if not queue:
        print('No')
        break
else:
    print('Yes')
    for i in range(1, n):
        print(sign[i] + 1)
