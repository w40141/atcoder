number = int(input())

count = 0
for num in range(1, number + 1, 2):
    divisor_num = 0
    for i in range(3, int(num / 2), 2):
        if num % i == 0:
            divisor_num += 1
    else:
        if divisor_num == 6:
            count += 1
print(count)
