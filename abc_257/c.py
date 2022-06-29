number_people = int(input())
is_adults = list(map(int, list(input())))
weights = list(map(int, input().split()))

pair = [(weight, is_adult) for weight, is_adult in zip(weights, is_adults)]
pair.sort(key=lambda x: x[0])
result = sum(is_adults)
x = result
for i in range(number_people):
    if pair[i][1] == 0:
        x += 1
    else:
        x -= 1
    if i < number_people - 1:
        if pair[i][0] != pair[i + 1][0]:
            result = max(result, x)
        else:
            pass
    else:
        result = max(result, x)
print(result)
