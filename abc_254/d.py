from typing import List


n = int(input())

# 自分×自分は平方数
ans = n
checked_num = [0]

i = 2
original_numbers: List[int] = []
# n 以下の平方数を出す
while i * i <= n:
    original_numbers.append(i * i)
    i += 1

i = 1
tmp_numbers = [1]
while len(tmp_numbers) > 0:
    if i in checked_num:
        i += 1
        continue
    tmp_numbers = list(filter(lambda y: y <= n, map(lambda x: x * i, original_numbers)))
    checked_num += [i] + tmp_numbers
    x = len(tmp_numbers)
    if x >= 2:
        ans += 2 * x
        ans += x * (x - 1)
    elif x == 1:
        ans += 2
    else:
        pass
    i += 1
print(ans)
