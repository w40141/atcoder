def prime_factorize(n):
    if n == 1:
        return [1]
    primes = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            primes.append(i)
            n //= i
        else:
            i += 1
    if n != 1:
        primes.append(n)
    return primes


n = int(input())
if n == 1:
    print(0)
    exit()
primes = set(prime_factorize(n))
ans = 0
for p in primes:
    for e in range(1, 10 ** 10):
        if n % (p**e) == 0:
            ans += 1
            n //= p ** e
        else:
            break
print(ans)
