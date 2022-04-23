s = list(input())

s_set = set(s)
if len(s) != len(s_set):
    print("No")
else:
    upper_counter = 0
    lower_counter = 0
    for si in s:
        if si.isupper():
            upper_counter += 1
        else:
            lower_counter += 1

    if upper_counter == 0 or lower_counter == 0:
        print("No")
    else:
        print("Yes")
