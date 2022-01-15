n = int(input())
h = map(int, input().split())
now = 0
for hi in h:
    if hi > now:
        now = hi
    else:
        break
print(now)
