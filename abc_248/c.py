n, m, k = map(int, input().split())
k = k - n

s = max(k, n)
t = min(k, n)
a = [i for i in range(k+n, s, -1)]
b = [i for i in range(1, t + 1)]
ans = 1
for a_i, b_i in zip(a, b):
    ans = (ans * a_i) // b_i % 998244353
print(ans)
