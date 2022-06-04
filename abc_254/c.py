n, k = map(int, input().split())
A = list(map(int, input().split()))
A += [10 ** 10 for _ in range(k - (n % k))]
numbers = [sorted([A[i] for i in range(j, len(A), k)]) for j in range(k)]

B = [numbers[i % k][i // k] for i in range(len(A))]

C = sorted(A)
if C == B:
    print('Yes')
else:
    print('No')
