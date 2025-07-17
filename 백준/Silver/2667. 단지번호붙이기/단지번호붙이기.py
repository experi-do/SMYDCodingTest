import sys

N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(x, y):
    stack = []
    stack.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (visited[nx][ny]==False) and (grid[nx][ny]==1):
                stack.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

answer = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            answer.append(dfs(i, j))

print(len(answer))
answer = sorted(answer)
for cnt in answer:
    print(cnt)
