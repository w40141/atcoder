h, w, k = map(int, input().split())
masu = [list(input()) for _ in range(h)]
ans = 0
for gyou in range(1 << h):
    for retu in range(1 << w):
        count = 0
        for g in range(h):
            for r in range(w):
                if gyou >> g & 1 and retu >> r & 1:
                    if masu[g][r] == "#":
                        count += 1
        if count == k:
            ans += 1
print(ans)
