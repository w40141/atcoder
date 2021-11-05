N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(W + 1)] for __ in range(N + 1)]

for w in range(W + 1):
    for i in range(N):
        wi, vi = items[i]
        if w >= wi:
            dp[i + 1][w] = max(dp[i][w - wi] + vi, dp[i][w])
        else:
            dp[i + 1][w] = dp[i][w]
print(dp[-1][-1])
