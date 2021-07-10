n = int(input())
num_list = list(map(int, input().split()))
num_list_sorted = sorted(num_list)
num_list_ans = [num - i for i, num in enumerate(num_list_sorted)]
a = 1
for num in num_list_ans:
    a *= num
    a %= 10 ** 9 + 7

print(a)
