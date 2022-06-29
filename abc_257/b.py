n, k, q = map(int, input().split())
a_li = [-1] + list(map(int, input().split()))
l_li = list(map(int, input().split()))

for l in l_li:
    if a_li[l] < n:
        if l == k:
            a_li[l] += 1
        else:
            if a_li[l] + 1 != a_li[l + 1]:
                a_li[l] += 1
print(' '.join(map(str, a_li[1:])))
