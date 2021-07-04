import math

p = int(input())

max_val = 10
for i in range(1, 11):
    a = math.factorial(i)
    if a > p:
        max_val = i - 1
        break
    else:
        pass

val = p
counter = 0
for i in range(max_val, 0, -1):
    a = math.factorial(i)
    while val >= a:
        counter += 1
        val -= a
print(counter)
