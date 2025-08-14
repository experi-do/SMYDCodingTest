import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)
visited = [0 for _ in range(n+1)]

for i in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

def prim(graph, start):
    visited[start] = 1
    candidate = graph[start]
    heapq.heapify(candidate)
    mst = []
    total = 0 

    while candidate:
        weight, u, v = heapq.heappop(candidate)
        if visited[v] == 0:
            visited[v] = 1
            mst.append((u, v))
            total += weight

            for edge in graph[v]: 
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)

    return total

print(prim(graph, 1))
