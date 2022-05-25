n = int(input())
i = 1
count = 0
while i * i <= 2 * n:
    if 2 * n % i == 0:
        m = 2 * n // i
        if i % 2 != m % 2:
            count += 2
    i += 1
print(count)
