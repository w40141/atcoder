import collections

def count(s_li, count):
    ans = 0
    for i in range(10000):
        _c = count
        check_li = [0 for _ in range(10)]
        a = "{:0>4d}".format(i)
        for ai in a:
            check_li[int(ai)] += 1
        for si, li in zip(s_li, check_li):
            if si == 'x' and li != 0:
                break
            elif si == 'o' and li == 0:
                break
            elif si == 'o' and li > 0:
                _c -= 1
            else:
                pass
        else:
            if _c == 0:
                ans += 1
            else:
                pass
    return ans

s = input()
s_li = list(s)
c = collections.Counter(s_li)
ans = 0
if c['o'] > 4:
    pass
elif c['o'] == 4:
    ans = 24
else:
    ans = count(s_li, c['o'])
print(ans)
