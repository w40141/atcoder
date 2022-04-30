n = int(input())
a = map(int, input().split())
b = map(int, input().split())
s = [ai * bi for ai, bi in zip(a, b)]
su = sum(s)
if su == 0:
    print("Yes")
else:
    print("No")
