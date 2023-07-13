n = int(input())
masu = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if masu[i][j] == 'W' and masu[j][i] == 'L':
            pass
        elif masu[i][j] == 'L' and masu[j][i] == 'W':
            pass
        elif masu[i][j] == 'D' and masu[j][i] == 'D':
            pass
        else:
            print('incorrect')
            exit()
print('correct')
