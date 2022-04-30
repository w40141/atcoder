n = int(input())
mountains = [input().split() for _ in range(n)]
first = 0
first_mountain = ''
second = 0
second_mountain = ''
for m in mountains:
    h = int(m[1])
    if h > first:
        second = first
        second_mountain = first_mountain
        first = h
        first_mountain = m[0]
    if h < first and h > second:
        second = h
        second_mountain = m[0]
print(second_mountain)
