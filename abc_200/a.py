n = int(input())
sec = int(n / 100)
if n > sec * 100:
    print(sec + 1)
else:
    print(sec)
