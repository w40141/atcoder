tmp = input()
tmp_li = list(map(int, tmp.split(' ')))
n = tmp_li[0]
k = tmp_li[1]

for _ in range(k):
    if n % 200 == 0:
        n = int(n / 200)
    else:
        n *= 1000
        n += 200
print(n)
