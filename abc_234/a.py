t = int(input())


def f(x: int) -> int:
    return x * x + 2 * x + 3


def ff(x: int) -> int:
    return f(f(x))


def ft(x: int) -> int:
    return f(x) + x


def fft(x: int) -> int:
    return f(ft(x))


def fff1(x: int) -> int:
    return f(fft(x) + ff(x))


print(fff1(t))
