import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

longest: int = 0
for first in range(n):
    for second in range(first + 1, n):
        first_x = points[first][0]
        first_y = points[first][1]
        second_x = points[second][0]
        second_y = points[second][1]
        length = (first_x - second_x) ** 2 + (first_y - second_y) ** 2
        if length > longest:
            longest = length
print(math.sqrt(longest))
