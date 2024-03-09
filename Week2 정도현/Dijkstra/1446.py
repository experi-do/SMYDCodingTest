import sys
input = sys.stdin.readline

from collections import defaultdict

n, total = map(int, input().split(' '))

graph = defaultdict(list)
for _ in range(n):
    start, end, cost = map(int, input().split(' '))
    if (end > total):
        continue
    graph[start].append((end, cost))

distance = [i for i in range(total + 1)]

for i in range(total+1):
    distance[i] = min(distance[i], distance[i-1]+1)

    for s, info in graph.items():
        for e, c in info:
            if i == s and distance[e] > distance[i]+c:
                distance[e] = distance[i]+c

print(distance[total])