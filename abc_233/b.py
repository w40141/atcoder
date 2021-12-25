left, right = map(int, input().split())
str = input()
str_left = str[: left - 1]
str_center = str[left - 1 : right]
str_right = str[right:]
print(str_left + str_center[::-1] + str_right)
