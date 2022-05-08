n, k = map(int, input().split())
H = [0] * (k + 1) + list(map(int, input().split()))

dp = [10 ** 15 for _ in range(n + k + 1)]
dp[k + 1] = 0
for i in range(2 + k, n + k + 1):
    tmp = 10 ** 15
    for j in range(1, k + 1):
        dp[i] = min(dp[i], dp[i - j] + abs(H[i] - H[i - j]))
print(dp[-1])
