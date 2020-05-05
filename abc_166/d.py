import itertools


max_num = 200
num_list = [i for i in range(-max_num,  max_num+1)]
num_comb = list(itertools.permutations(num_list, 2))

x = int(input().strip())
for comb in num_comb:
    a = comb[0]
    b = comb[1]
    # print(a, b)
    a5 = a ** 5
    b5 = b ** 5
    if a5 - b5 == x:
        print(a, b)
        break
