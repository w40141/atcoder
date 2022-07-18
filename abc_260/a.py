s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for k, v in d.items():
    if v == 1:
        print(k)
        break
else:
    print(-1)
