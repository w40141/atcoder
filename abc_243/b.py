n = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

same_num = 0
for a, b in zip(a_li, b_li):
    if a == b:
        same_num += 1

a_s = set(a_li)
b_s = set(b_li)
c = a_s & b_s
print(same_num)
print(len(c) - same_num)
