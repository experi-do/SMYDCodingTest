import sys
import queue

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

max_area = 0
total_cnt = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(y, x):
    area = 1
    q.put((y, x))
    while not q.empty():
        y, x = q.get()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.put((ny, nx))
                    area += 1

    return area


q = queue.Queue()

for i in range(n):
    for j in range(m):
        if (grid[i][j] == 1) and (visited[i][j] == False):
            visited[i][j] = True
            total_cnt += 1
            max_area = max(max_area, bfs(i, j))

print(total_cnt)
print(max_area)