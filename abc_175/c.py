now, count, distance = map(int, input().split())
if abs(now) > distance * count:
    print(abs(now) - distance * count)
else:
    new_now = now + count * distance
    mod = new_now % (2 * distance)
    if mod > distance:
        print(2 * distance - mod)
    else:
        print(mod)
