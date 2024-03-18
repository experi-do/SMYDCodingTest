import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
dist = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

current = cost[0]
ans = 0

for i in range(1, len(cost)):
    ans += dist[i-1]*current
    if current > cost[i]:
        current = cost[i]
print(ans)


