n = int(input())

def factorial(n: int, i: int) -> int:
    a: int = 1
    b: int = 1
    if n == 0:
        return 1
    else:
        for j in range(i):
            a *= (n - j)
            b *= (i - j)
        return a // b


for i in range(n):
    ans = map(str, [factorial(i, j) for j in range(i + 1)])
    print(' '.join(ans))
