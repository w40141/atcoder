from collections import Counter


n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    d = Counter(a[l - 1: r + 1])
    print(d[x])
