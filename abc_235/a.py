s = input()

x = int(s[0]) * 100 + int(s[1]) * 10 + int(s[2])
y = int(s[1]) * 100 + int(s[2]) * 10 + int(s[0])
z = int(s[2]) * 100 + int(s[0]) * 10 + int(s[1])
print(x + y + z)
