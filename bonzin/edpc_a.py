n = int(input())
H = [0] + list(map(int, input().split()))

dp = [10 ** 15 for _ in range(n + 1)]
dp[1] = 0
dp[2] = abs(H[2] - H[1])
for i in range(3, n + 1):
    cost1 = dp[i-1] + abs(H[i] - H[i-1])
    cost2 = dp[i-2] + abs(H[i] - H[i-2])
    dp[i] = min(cost1, cost2)
print(dp[n])
