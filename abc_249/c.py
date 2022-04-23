from itertools import chain, combinations
import collections


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


n, k = map(int, input().split())
s_li = [tuple(input()) for _ in range(n)]

counter = 0
dic = {chr(i): 0 for i in range(97, 123)}
for s in powerset(s_li):
    x = chain.from_iterable(s)
    li = collections.Counter(x)
    tmp_counter = 0
    for key in li.values():
        if k == key:
            tmp_counter += 1
    if tmp_counter > counter:
        counter = tmp_counter
    else:
        pass
print(counter)
