n, m = map(int, input().split())
station_s = input().split()
station_t = input().split()

s_i = 0
t_i = 0
while s_i != n and t_i != m:
    if station_s[s_i] == station_t[t_i]:
        print("Yes")
        s_i += 1
        t_i += 1
    else:
        print("No")
        s_i += 1
