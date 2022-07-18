n, x, y = map(int, input().split())


# true -> blue
# false -> red
def counter(level: int, color: bool, count: int):
    tmp = 0
    if level <= 1:
        return count if color else 0
    if color:
        tmp += counter(level - 1, not color, count)
        tmp += counter(level - 1, color, count * y)
    else:
        tmp += counter(level - 1, color, count)
        tmp += counter(level, not color, count * x)
    return tmp


print(counter(n, False, 1))
