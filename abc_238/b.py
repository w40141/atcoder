n = int(input())
kakudo_map = map(int, input().split())

en = [0 for _ in range(360)]
en[0] = 1

start = 0
for kakudo in kakudo_map:
    start += kakudo
    start = start % 360
    en[start] = 1
s = "".join(map(str, en))
s_li = s.split("1")
t = map(len, s_li)
print(max(t) + 1)
