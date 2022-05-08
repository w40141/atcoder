from collections import deque

S = input().split()
s_deque = deque(S)
q = int(input())
flag = False
for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        flag = not flag
    else:
        if query[1] == "1" and not flag:
            s_deque.appendleft(query[2])
        elif query[1] == "2" and not flag:
            s_deque.append(query[2])
        elif query[1] == "1" and flag:
            s_deque.append(query[2])
        else:
            s_deque.appendleft(query[2])
ans = "".join(s_deque)
if flag:
    ans = ans[::-1]
print(ans)
