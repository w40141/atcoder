n = int(input())
count = n
for i in range(1, n + 1):
    num_str = list(str(i))
    num_oct = list(str(oct(i)))[2:]
    if '7' in num_str or '7' in num_oct:
        count -= 1
print(count)
