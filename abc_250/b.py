n, a, b = map(int, input().split())


def make_black(a, b):
    return ["#" * b for _ in range(a)]


def make_white(a, b):
    return ["." * b for _ in range(a)]


def make(is_white, a, b):
    if is_white:
        return make_white(a, b)
    else:
        return make_black(a, b)


for m, i in enumerate(range(n)):
    is_white = True if m % 2 == 0 else False
    sub_ans = ["" for _ in range(a)]
    for j in range(n):
        tmp = make(is_white, a, b)
        for s, t in enumerate(tmp):
            sub_ans[s] += t
        is_white = not is_white
    print('\n'.join(sub_ans))
