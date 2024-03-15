import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
store = []
min_sets = int(1e9)
min_single = int(1e9)
for _ in range(m):
    sets, single = map(int, input().split(' '))
    store.append((sets, single))
    if min_sets > sets:
        min_sets = sets
    if min_single > single:
        min_single = single

set_num = n // 6
remaining = n - (set_num*6)
total_price = 0
if min_sets < min_single*6:
    if (remaining*min_single > min_sets):
        set_num += 1
        total_price = set_num * min_sets
    else:
        total_price = set_num * min_sets + remaining * min_single
else:
    total_price = n * min_single
print(total_price)

