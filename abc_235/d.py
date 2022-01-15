a, n = map(int, input().split())


class div:
    def __init__(
        self, a: int, n: int, wasTurn: bool = False, count: int = 0, fin: bool = False
    ):
        self.a = a
        self.n = n
        self.wasTurn = wasTurn
        self.count = count
        self.fin = fin

    def __str__(self):
        return f"a: {self.a}, n: {self.n}, wasTurn: {self.wasTurn}, count: {self.count}"

    def turn(self):
        if 0 > self.n or self.n % 10 == 0:
            return div(self.a, self.n, False, self.count)
        else:
            n_str = str(self.n)
            new_n = n_str[1:] + n_str[0]
            return div(self.a, int(new_n), True, self.count + 1)

    def divide(self):
        if self.n % self.a == 0:
            dived = self.n // self.a
            if dived == 1:
                return div(self.a, 1, False, self.count + 1, True)
            else:
                return div(self.a, dived, False, self.count + 1)
        else:
            return div(self.a, -1, False, -1, True)


def tmp(first):
    if first.wasTurn:
        print(first)
        first_dived = first.divide()
        print(first_dived)
        if first_dived.fin:
            ans = first_dived.count
        else:
            ans = tmp(first_dived)
    else:
        print(first)
        first_turned = first.turn()
        print(first_turned)
        first_dived = first_turned.divide()
        print(first_dived)
        if first_dived.fin:
            ans = first_dived.count
        else:
            ans = tmp(first_dived)
    return ans


first = div(a, n)


print(tmp(first))
