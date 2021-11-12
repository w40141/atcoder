N = int(input())
masu_list = list(map(int, input().split()))


def how_many_move_to_right_in_masu_list() -> int:
    now_move: int = 0
    index: int = 0
    while N > index:
        new_move: int = 0
        while N > index + 1 and masu_list[index] >= masu_list[index + 1]:
            index += 1
            new_move += 1
        now_move = max(now_move, new_move)
        index += 1
    return now_move


print(how_many_move_to_right_in_masu_list())
