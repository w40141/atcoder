raw_input = int(input().strip())
num = raw_input % 10
if num == 3:
    print('bon')
elif num in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')
