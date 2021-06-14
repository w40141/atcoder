n = int(input())
a_list = list(map(int, input().split()))

n_list = list(range(1, n + 1))
a_sorted = sorted(a_list)
if (n_list == a_sorted):
    print('Yes')
else:
    print('No')
