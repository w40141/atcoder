n, k = map(int, input().split())
p_list = list(map(int, input().split()))


min_card = p_list[0]
field = [[p_list[0]]]
eaten_cards = [-1 for _ in range(n + 1)]
for i, p in enumerate(p_list[1:], 2):
    if p < min_card:
        min_card = p
        field[0].append(p)
    else:
        field.append([p])
    if len(field[0]) == k:
        numbers = field[0]
        for number in numbers:
            eaten_cards[number] = i
        field = field[1:]
        if len(field) == 0:
            min_card = 10 ** 6
            field = [[]]
        else:
            min_card = field[0][0]

for i in range(n):
    print(eaten_cards[i + 1])
