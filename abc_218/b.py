p = map(int, input().split())

s = ""
for pi in p:
    s += chr(ord("a") + pi - 1)

print(s)
