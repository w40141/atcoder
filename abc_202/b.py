string = input()


def tern_str(s):
    if '6' == s:
        return '9'
    elif '9' == s:
        return '6'
    else:
        return s


ans = ''
for s in string:
    ans += tern_str(s)

print(ans[::-1])
