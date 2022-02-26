n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = True
for bi in b:
    try:
        index = a.index(bi)
        a[index] = 0
    except:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
