num = list(map(int, input().split()))
n = num[0]
m = num[1]
q = num[2]

seisu_list = [[1 for _ in range(n)] for __ in range(q)]
count = 0

for i in range(q):
    num = list(map(int, input().split()))
    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    seisu_list[count][3] = seisu_list[count][1] + c
