import math

n, a, b = map(int, input().split())

n_sum = n * (n + 1) >> 1
a_sum = (n // a) * (a + (n // a) * a) >> 1
b_sum = (n // b) * (b + (n // b) * b) >> 1
c = a * b // math.gcd(a, b)
c_sum = (n // c) * (c + (n // c) * c) >> 1
ans = n_sum - a_sum - b_sum + c_sum
print(ans)
