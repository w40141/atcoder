x = int(input())

for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        if x == i ** 5 - j ** 5:
            print(str(i) + " " + str(j))
            exit()
