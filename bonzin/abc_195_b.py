a, b, w = map(int, input().split())
wg = 1000 * w

max_ans = -10 ** 15
min_ans = 10 ** 15

for i in range(1, 10 ** 6 + 10):
    if a * i <= wg <= b * i:
        max_ans = max(max_ans, i)
        min_ans = min(min_ans, i)

if min_ans == 10 ** 15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
