n = int(input())


def s(n):
    if n == 1:
        return "1 "
    else:
        return s(n - 1) + str(n) + " " + s(n - 1)


print(s(n)[:-1])
