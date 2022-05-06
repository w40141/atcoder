n, k = map(int, input().split())
P = list(map(int, input().split()))


def p(n):
    return (1 + n) / 2


kitaichi = list(map(p, P))
k_cum_sum = [kitaichi[0]]
for i in range(1, n):
    k_cum_sum.append(k_cum_sum[i - 1] + kitaichi[i])
ans = -10 ** 15
for i in range(n - k + 1):
    if i:
        ans_tmp = k_cum_sum[i + k - 1] - k_cum_sum[i - 1]
    else:
        ans_tmp = k_cum_sum[i + k - 1]
    ans = max(ans_tmp, ans)
print(ans)
