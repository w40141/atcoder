n, k = map(int, input().split())
ps = list(map(int, input().split()))

for i in range(n - k + 1):
    sub_list = ps[:i + k]
    sorted_list = sorted(sub_list)
    print(sorted_list[i])
