w = int(input())
print(99 * 3)
ans = []
for i in range(1, 100):
    a = i
    b = 100 * i
    c = 10000 * i
    ans.append(str(a))
    ans.append(str(b))
    ans.append(str(c))
print(" ".join(ans))
