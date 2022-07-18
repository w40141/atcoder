n, x, y, z = map(int, input().split())
math = list(map(int, input().split()))
math_points = sorted([(i + 1, math[i])
                     for i in range(n)], key=lambda x: x[1], reverse=True)
eng = list(map(int, input().split()))
eng_points = sorted([(i + 1, eng[i]) for i in range(n)],
                    key=lambda x: x[1], reverse=True)
all_points = sorted([(i + 1, math[i] + eng[i])
                    for i in range(n)], key=lambda x: x[1], reverse=True)
passed = []

for i in range(x):
    passed.append(math_points[i][0])

i = 0
c = 0
while c < y:
    tmp = eng_points[i][0]
    if tmp in passed:
        pass
    else:
        passed.append(eng_points[i][0])
        c += 1
    i += 1

c = 0
i = 0
while c < z:
    tmp = all_points[i][0]
    if tmp in passed:
        pass
    else:
        passed.append(all_points[i][0])
        c += 1
    i += 1

passed.sort()
for p in passed:
    print(p)
