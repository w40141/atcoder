N = int(input())
n = 0
for a in range(1, N + 1):
    if a * a * a > N:
        break
    for b in range(a, N + 1):
        if b * b > N / a:
            break
        n += N // a // b - b + 1
print(n)
