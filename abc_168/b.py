k = int(input().strip())
s = input().strip()
len_s = len(s)
if k < len_s:
    print(s[:k] + '...')
else:
    print(s)
