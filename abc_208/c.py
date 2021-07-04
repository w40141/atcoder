tmp = list(map(int, input().split()))
n = tmp[0]
k = tmp[1]

a = list(map(int, input().split()))
a_sort = sorted(a)

byodo = k // n
amari = k % n

ans = dict()
for i in a_sort[:amari]:
    ans[i] = byodo + 1

for i in a_sort[amari:]:
    ans[i] = byodo

for i in a:
    print(ans[i])
