import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def countIce():
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt


answer = 0
while True:
    ice_count = countIce()
    if ice_count >= 2:
        print(answer)
        break
    if ice_count == 0:
        print(0)
        break

    answer += 1
    melt_amounts = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                water_cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        water_cnt += 1
                melt_amounts[i][j] = water_cnt
                
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                grid[i][j] = max(0, grid[i][j] - melt_amounts[i][j])