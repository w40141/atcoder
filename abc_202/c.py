import collections


n = int(input())
a_counter = collections.Counter(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
b_counter = collections.Counter([b_list[c - 1] for c in c_list])

counter = 0
for key, value in a_counter.items():
    if key in b_counter:
        counter += value * b_counter[key]

print(counter)
