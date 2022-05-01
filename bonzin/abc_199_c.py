N = int(input())
S = list(input())
Q = int(input())


flag = False
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flag:
            if a < N:
                a += N
            else:
                a -= N
            if b < N:
                b += N
            else:
                b -= N
        S[a], S[b] = S[b], S[a]
    else:
        flag = not flag
else:
    if flag:
        S = S[N:] + S[:N]
print("".join(S))
