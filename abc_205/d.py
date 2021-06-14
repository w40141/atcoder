tmp = list(map(int, input().split()))
n = tmp[0]
q = tmp[1]
a_set = set(map(int, input().split()))

for i in range(q):
    ans_set = set()
    k = int(input())
    l_k = k
    while len(ans_set) != k:
        ans_set = ans_set | set(range(1, l_k + 1))
        ans_set -= a_set
        l_k += (k - len(ans_set))
    print(max(ans_set))
