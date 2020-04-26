raw_input = input().split()
n = int(raw_input[0])
items = [input().strip() for _ in range(n)]
items = set(items)
print(len(items))
