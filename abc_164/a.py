raw_input = input().split()
s = int(raw_input[0])
w = int(raw_input[1])
if s - w > 0:
    print('safe')
else:
    print('unsafe')
