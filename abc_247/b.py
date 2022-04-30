n = int(input())
people = [input().split(" ") for _ in range(n)]


def check(people):
    for i, p in enumerate(people):
        sei_p = p[0]
        mei_p = p[1]
        sei_flag = False
        mei_flag = False
        for j, q in enumerate(people):
            if i == j:
                continue
            sei_q = q[0]
            mei_q = q[1]
            if sei_p == sei_q or sei_p == mei_q:
                sei_flag = True
            if mei_p == sei_q or mei_p == mei_q:
                mei_flag = True
            if sei_flag and mei_flag:
                return "No"
    return "Yes"


print(check(people))
