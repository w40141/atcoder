from typing import Dict, List, Tuple

n = int(input())
people: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(n)]
s_li = list(input())

left_max_dic: Dict[int, Tuple[int, int]] = {}
right_min_dic: Dict[int, Tuple[int, int]] = {}
for p, s in zip(people, s_li):
    x = p[0]
    y = p[1]
    if s == "L":
        if y in left_max_dic:
            if x > left_max_dic[y][0]:
                left_max_dic[y] = p
        else:
            left_max_dic[y] = p
    else:
        if y in right_min_dic:
            if x < right_min_dic[y][0]:
                right_min_dic[y] = p
        else:
            right_min_dic[y] = p
for k, v in right_min_dic.items():
    if k in left_max_dic:
        if v[0] < left_max_dic[k][0]:
            print('Yes')
            break
    else:
        pass
else:
    print('No')
