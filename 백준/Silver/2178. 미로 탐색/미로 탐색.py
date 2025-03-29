import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

queue = deque([(0, 0)])  # Start with the top-left corner
visited[0][0] = True
cnt = 0

# Perform BFS
while queue:
    cnt += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()

        # Check if we've reached the bottom-right corner
        if y == n - 1 and x == m - 1:
            print(cnt)
            sys.exit()

        # Explore the 4 possible directions
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

# If no path is found to the bottom-right corner
print(-1)
