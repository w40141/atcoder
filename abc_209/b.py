tmp = list(map(int, input().split()))
n = tmp[0]
x = tmp[1]

a_tmp = map(int, input().split())
a_list = [a - 1 if i % 2 else a for i, a in enumerate(a_tmp)]

if sum(a_list) <= x:
    print("Yes")
else:
    print("No")
