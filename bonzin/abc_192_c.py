k, n = map(int, input().split())


def g1(x: int) -> int:
    x_str = list(str(x))
    n = sorted(x_str, reverse=True)
    return int("".join(n))


def g2(x: int) -> int:
    x_str = list(str(x))
    n = sorted(x_str)
    return int("".join(n))


def f(x: int) -> int:
    return g1(x) - g2(x)


for _ in range(n):
    k = f(k)
print(k)
