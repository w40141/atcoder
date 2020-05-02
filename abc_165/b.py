x = int(input().strip())
a = 100
rishi = 1.01
count = 0
while a < x:
    count += 1
    a = int(a * rishi)
print(count)
