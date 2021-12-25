import math

# x = int(input())
x = 10 ** 50000
ans = x
keta = math.log10(x)
ans_list = [x // (10 ** i) for i in range(int(keta) + 1)]
print(sum(ans_list))
