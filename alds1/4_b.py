n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))


# def binary_search(searched_li, search_number):
#     if searched_li == []:
#         return False
#     else:
#         index = int(len(searched_li) / 2)
#         index_number = searched_li[index]
#         if index_number == search_number:
#             return True
#         elif index_number < search_number:
#             return binary_search(searched_li[index + 1:], search_number)
#         else:
#             return binary_search(searched_li[:index], search_number)


def binary_search(searched_li, search_number):
    li = list(searched_li)
    while li != []:
        index = int(len(li) / 2)
        if li[index] == search_number:
            return True
            break
        elif li[index] < search_number:
            li = li[index + 1:]
        else:
            li = li[:index]
    return False


ans = sum([binary_search(s, i) for i in t])
print(ans)
