import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

answer = []

for i in range(1, n+1):
    visited = [False] * (n + 1)
    bacon = [0] * (n + 1)
    queue = deque([i])
    visited[i] = True

    while queue:
        current = queue.popleft()
        for neighbor in grid[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                bacon[neighbor] = bacon[current] + 1
                queue.append(neighbor)

    answer.append(sum(bacon))

min_value = min(answer)
print(answer.index(min_value) + 1)