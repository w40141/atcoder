n = int(input())
numbers = list(map(int, input().split()))
ans = 0

count = 0
for i, number in enumerate(numbers, 1):
    if i == number:
        count += 1
ans += count * (count - 1) // 2

tmp = 0
for i, number in enumerate(numbers, 1):
    if i == numbers[number - 1]:
        tmp += 1
ans += tmp // 2 - count // 2
print(ans)
