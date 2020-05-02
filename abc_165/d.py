def f(a, b, x):
    return int(a * x / b) - a * int(x / b)


num = list(map(int, input().split()))
a = num[0]
b = num[1]
n = num[2]
x = (int(n/b) + 1) * b - 1
max_num = f(a, b, min(b-1, n))
print(max_num)
