import heapq

n, k, x = map(int, input().split())
a_li = list(map(int, input().split()))

mod_li = [a % x for a in a_li]
mod_sum = sum(mod_li)
sho_li = [a // x for a in a_li]
sho_sum = sum(sho_li)
if k >= sho_sum + n:
    print(0)
else:
    add_sho = k - sho_sum
    if add_sho > 0:
        new_mod_li = [-1 * m for m in mod_li]
        heapq.heapify(new_mod_li)
        for _ in range(add_sho):
            m = heapq.heappop(new_mod_li)
            m = min(0, m + x)
            heapq.heappush(new_mod_li, m)
        print(sum(new_mod_li) * -1)
    else:
        print(-1 * add_sho * x + mod_sum)
