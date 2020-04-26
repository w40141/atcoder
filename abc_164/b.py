raw_input = input().split()

takahashi_hp = int(raw_input[0])
takahashi_ak = int(raw_input[1])
aoki_hp = int(raw_input[2])
aoki_ak = int(raw_input[3])

while 1:
    aoki_hp -= takahashi_ak
    if aoki_hp <= 0:
        print('Yes')
        break
    takahashi_hp -= aoki_ak
    if takahashi_hp <= 0:
        print('No')
        break
