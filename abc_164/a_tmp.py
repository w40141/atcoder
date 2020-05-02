raw_input = input().split()
s = int(raw_input[0])
w = int(raw_input[1])
t = 0
if s - w > 0:
    print('safe')
else:
    print('unsafe')


def add(a, b):
    return a + b


def f():
    return add(None, 0)

def add(a, b):
    c = a if a else 0
    return a+ b
