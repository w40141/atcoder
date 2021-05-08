# import sys
# def input():
#     return sys.stdin.readline()[:-1]

n = int(input())
num_li = list(map(int, input().split()))
org = [0 for i in range(200)]
for n in num_li:
    org[n%200] += 1

num = 0
for o in org:
    if o:
        num += o * (o-1) / 2
# for i in range(n):
#     for j in range(i+1, n):
#         a = num_li[i] - num_li[j]
#         if a % 200 == 0:
#             num += 1
print(int(num))
