n = int(input())
A = list(map(int, input().split()))
ans = - 10 ** 15

for left in range(n):
    a_min = A[left]
    for right in range(left, n):
        a_min = min(a_min, A[right])
        ans = max(ans, a_min * (right - left + 1))
print(ans)
