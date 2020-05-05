raw_input = list(map(int, input().split()))
n = raw_input[0]
k = raw_input[1]
sunuke = [0 for _ in range(n)]
for i in range(k):
    d = int(input().strip())
    a = list(map(int, input().split()))
    for j in a:
        sunuke[j-1] += 1
counter = 0
for i in sunuke:
    if i == 0:
        counter += 1
print(counter)
