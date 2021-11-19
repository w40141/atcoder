n = int(input())
A = map(int, input().split())

count = 0
for a in A:
    tmp = a
    while not (tmp & 1):
        count += 1
        tmp >>= 1
print(count)
