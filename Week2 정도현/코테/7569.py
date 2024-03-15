import sys
sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split(' '))
grid = [[list(map(int, input().split(' '))) for _ in range(n)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 1:
                q.append((i, j, k))

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = grid[z][x][y] + 1
                q.append((nz, nx, ny))


isDone = True
total = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 0:
                total = -1
                isDone = False
            else:
                total =  max(total, grid[i][j][k])
if isDone:
    print(total - 1)
else:
    print(-1)
