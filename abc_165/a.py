k = int(input().strip())
num = list(map(int, input().split()))
count = k
while 1:
    if num[0] <= k <= num[1]:
        print('OK')
        break
    elif num[1] < k:
        print('NG')
        break
    else:
        k += count
