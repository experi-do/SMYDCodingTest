from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

city = int(input())
bus = int(input())

info = defaultdict(list)
cost_dict = defaultdict(lambda: float('inf'))

for _ in range(bus):
    s, e, c = map(int, input().split(' '))
    info[s].append((e,c))

src, dst = map(int, input().split(' '))

def dijkstra(src, dst):
    Q = [(0, src)]

    while Q:
        cost, start = heapq.heappop(Q)
        if start == dst:
            return cost

        for e, c in info[start]:
            if cost + c < cost_dict[e]:
                cost_dict[e] = cost + c
                heapq.heappush(Q, (cost+c, e))

print(dijkstra(src, dst))