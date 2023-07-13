n = int(input())
words = {}

for i in range(n):
    s = input()
    if s in words:
        print(s + "(" + str(words[s]) + ")")
        words[s] += 1
    else:
        print(s)
        words[s] = 1
