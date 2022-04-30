n, x = map(int, input().split())
s_li = list(input())

x_bin = list(bin(x))
for s in s_li:
    if s == 'U':
        x_bin.pop()
    if s == 'L':
        x_bin.append('0')
    if s == 'R':
        x_bin.append('1')
print(int(''.join(x_bin), 2))
