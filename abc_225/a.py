s = input()

a = s[0]
b = s[1]
c = s[2]

if a == b == c:
    print(1)
elif a == b or b == c or c == a:
    print(3)
else:
    print(6)
