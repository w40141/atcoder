n, q = map(int, input().split())
numbers = [i for i in range(n + 1)]

for __ in range(q):
    print(numbers)
    x = int(input())
    tmp = numbers[x]
    if tmp >= n:
        numbers[x] -= 1
        numbers[tmp] += 1
    else:
        numbers[x] += 1
        numbers[tmp] -= 1
