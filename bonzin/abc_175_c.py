x, k, d = map(int, input().split())
# 7 4 3

ans = 0
x = abs(x)
num_a = x // d  # 7 // 3 = 2

if k % 2 == num_a % 2:
    if k > num_a:
        ans = x - d * num_a
    else:
        ans = abs(x - d * k)
else:
    if k > num_a + 1:
        ans = abs(x - d * (num_a + 1))
    else:
        ans = abs(x - d * k)

print(ans)
