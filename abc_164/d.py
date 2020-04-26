str_num = input().strip()
keta = len(str_num)
count = 0
for start in range(keta-3):
    for end in range(start+5, keta+1):
        num = int(str_num[start:end])
        if num % 2019 == 0:
            count += 1
            break

print(count)
