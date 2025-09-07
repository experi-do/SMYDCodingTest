import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]

visited = [[-1]*c for _ in range(r)]
jq = deque()
fq = deque()

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'J':
            jq.append((i, j))
            visited[i][j] = 0
        elif grid[i][j] == 'F':
            fq.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while jq:
    for _ in range(len(fq)):
        c_r, c_c = fq.popleft()
        for k in range(4):
            nr, nc = c_r + dr[k], c_c + dc[k]
            if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] != '#' and grid[nr][nc] != 'F':
                grid[nr][nc] = 'F'
                fq.append((nr, nc))

    for _ in range(len(jq)):
        r0, c0 = jq.popleft()

        if r0 == 0 or r0 == r-1 or c0 == 0 or c0 == c-1:
            print(visited[r0][c0] + 1)
            sys.exit(0)

        for k in range(4):
            nr, nc = r0 + dr[k], c0 + dc[k]
            if 0 <= nr < r and 0 <= nc < c:
                if grid[nr][nc] != '#' and grid[nr][nc] != 'F' and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r0][c0] + 1
                    jq.append((nr, nc))

print("IMPOSSIBLE")
