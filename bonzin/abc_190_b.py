n, s, d = map(int, input().split())
spell = [tuple(map(int, input().split())) for _ in range(n)]
for si in spell:
    if si[0] >= s or si[1] <= d:
        pass
    else:
        print("Yes")
        break
else:
    print("No")
