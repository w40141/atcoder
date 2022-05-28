import heapq
from collections import defaultdict
from typing import Dict, List


Q = int(input())
dic_num: Dict[str, int] = defaultdict(lambda: 0)
max_li: List[int] = []
min_li: List[int] = []
heapq.heapify(max_li)
heapq.heapify(min_li)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if str(x) not in dic_num:
            heapq.heappush(max_li, -x)
            heapq.heappush(min_li, x)
        dic_num[str(x)] += 1
    elif query[0] == 2:
        x = query[1]
        y = dic_num.get(str(x), 0)
        c = min(y, query[2])
        dic_num[str(x)] -= c
    else:
        num = [int(key) for key, value in dic_num.items() if value > 0]
        min_num = heapq.heappop(min_li)
        while min_num not in num:
            min_num = heapq.heappop(min_li)
        max_num = -heapq.heappop(max_li)
        while max_num not in num:
            max_num = -heapq.heappop(max_li)
        print(max_num - min_num)
        heapq.heappush(min_li, min_num)
        heapq.heappush(max_li, -max_num)
