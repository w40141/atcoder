N = int(input())
masu_list = list(map(int, input().split()))


def how_many_move_to_right(start: int) -> int:
    now_hight: int = masu_list[start]
    move: int = 0
    for new_hight in masu_list[start + 1 :]:
        if now_hight >= new_hight:
            move += 1
            now_hight = new_hight
        else:
            break
    return move


def how_many_move_to_right_in_masu_list() -> int:
    now_move: int = 0
    start: int = 0
    while start < N:
        new_move: int = how_many_move_to_right(start)
        now_move = max(now_move, new_move)
        start += new_move + 1
    return now_move


print(how_many_move_to_right_in_masu_list())
