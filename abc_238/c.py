n = int(input())

ans = 0
num = 10
num_li = [1]
while True:
    print(num_li)
    if n > num:
        num_li.append(num - num_li[-1])
        ans += int(
            (sum(num_li) - 1) * (num + (num // 10 + 1)) // 2 - num_li[-1] * (num // 10)
        )
    else:
        ans += int(
            (n - (sum(num_li) - 1)) * (n + 1 + (num // 10 + 1)) // 2
            - (n - num_li[-1]) * (num // 10)
        )
        break
    print(ans)
    num *= 10

print(ans % 998244353)
