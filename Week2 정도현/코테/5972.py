from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

road = defaultdict(list)
cost_dict = defaultdict(lambda:float('inf'))

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    road[a].append((b, c))
    road[b].append((a, c))
def dijkstra(src: int, dst: int):

    Q = [(0,src)]
    discovered=[src]

    while Q:
        cost, start = heapq.heappop(Q)
        if (start == dst):
            return cost

        for b, c in road[start]:
            if (cost + c < cost_dict[b]):
                cost_dict[b] = cost + c
                heapq.heappush(Q, (cost+c, b))
                discovered.append(b)




print(dijkstra(1, n))
