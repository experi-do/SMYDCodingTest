from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(n):
    queue = deque()
    queue.append((0, 0, n))
    visited = [[[0] * (n + 1) for _ in range(M)] for _ in range(N)]
    while queue:
        x, y, K = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][K]

        if K > 0:
            for k in range(8):
                nx = x + horse_dx[k]
                ny = y + horse_dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] != 1 and visited[nx][ny][K-1] == 0:
                        visited[nx][ny][K-1] = visited[x][y][K] + 1
                        queue.append((nx, ny, K-1))

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 1 and visited[nx][ny][K] == 0:
                    visited[nx][ny][K] = visited[x][y][K] + 1
                    queue.append((nx, ny, K))
    return -1

result = bfs(K)
print(result)