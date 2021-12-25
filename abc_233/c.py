n, x = map(int, input().split())
fukuro_tmp = [list(map(int, input().split())) for _ in range(n)]
kosu_list = [tmp[0] for tmp in fukuro_tmp]
fukuro = [tmp[1:] for tmp in fukuro_tmp]

ans_list = [x]
for f in fukuro:
    tmp_list = [[ans // i for ans in ans_list if (ans % i == 0) and (ans // i != 0)] for i in f]
    ans_list = [item for li in tmp_list for item in li]
print(ans_list.count(1))
