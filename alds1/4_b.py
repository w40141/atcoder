n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))


def binary_search(searched_li, search_number):
    return _binary_search(searched_li, search_number, int(len(searched_li) / 2))


def _binary_search(searched_li, search_number, index):
    if searched_li == []:
        return False
    else:
        index_number = searched_li[index]
        if index_number == search_number:
            return True
        elif index_number < search_number:
            return binary_search(searched_li[index + 1:], search_number)
        else:
            return binary_search(searched_li[:index], search_number)


ans = sum([binary_search(s, i) for i in t])
print(ans)
