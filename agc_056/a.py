N = int(input())

num_list = list(range(n))


def make_str(n):
    if N - n == 2:
        s = "##" + "." * (N - 3) + "#"
    elif N - n == 1:
        s = "#" + "." * (N - 3) + "##"
    else:
        s = ""
        for i in range(N - 3):
            if i == n:
                s += "###"
            else:
                s += "."
    return s

def check_num(i, j):
    tmp = j - i
    if :
        pass

def check(num_list):
    cluster = [[] for _ in range(N)]
    counter = 0
    for i, num in enumerate(num_list):
        if num >= N - 2:
            cluster[i + counter]
            counter += 1
        cluster[i + counter].append(num)
