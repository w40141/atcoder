s = input()

s_new = ""
sento = ""
for i, si in enumerate(s):
    if si == "a":
        sento += si
        continue
    else:
        s_new = s[i:]
        break

s_rev = s_new[::-1]
s_new = ""
usiro = ""
for i, si in enumerate(s_rev):
    if si == "a":
        usiro += si
        continue
    else:
        s_new = s_rev[i:]
        break

if s_new == s_new[::-1]:
    flag = True
else:
    flag = False

if flag:
    if s_new == "":
        print("Yes")
    elif len(usiro) >= len(sento):
        print("Yes")
    else:
        print("No")
else:
    print("No")
