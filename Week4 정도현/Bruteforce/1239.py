import sys
input = sys.stdin.readline

from itertools import permutations

n = int(input())
part = list(map(int, input().split(' ')))

part_comb = list(permutations(part, n))

def count(lst):
    cnt = 0
    for i in range(n-1, -1, -1):
        for k in range(i):
            if lst[i] - lst[k] == 50:
                cnt += 1
    return cnt

sum = 0
sum_part = []
answer = 0
for i in range(len(part_comb)):
    sum = 0
    sum_list = []
    for j in range(n):
        sum += part_comb[i][j]
        sum_list.append(sum)
    sum_part.append(sum_list)
    answer = max(answer, count(sum_list))
print(answer)

