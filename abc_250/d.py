n = int(input())


def check(n, prime_numbers, q):
    count = 0
    is_done = False
    for p in prime_numbers:
        if n >= p * q * q * q:
            count += 1
        else:
            is_done = True
            break
    return is_done, count


q = 3
prime_numbers = [2]
is_done = False
count = 0
while n // 2 >= q * q * q or not is_done:
    for p in prime_numbers:
        if p * p > q:
            is_done, tmp = check(n, prime_numbers, q)
            count += tmp
            if not is_done:
                prime_numbers.append(q)
            break
        if q % p == 0:
            break
        else:
            pass
    else:
        is_done, tmp = check(n, prime_numbers, q)
        count += tmp
        if is_done:
            pass
        else:
            prime_numbers.append(q)

        prime_numbers.append(q)
    q += 2
print(count)
