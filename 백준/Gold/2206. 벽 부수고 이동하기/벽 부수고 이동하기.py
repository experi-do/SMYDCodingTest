import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

class Node:
    def __init__(self, x, y, isUsed):
        self.x = x
        self.y = y
        self.isUsed = isUsed

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
answer = [[0] * M for _ in range(N)]

queue = deque()
start = Node(0, 0, 0)
queue.append(start)
visited[0][0][0] = True
answer[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    node = queue.popleft()
    cx, cy, c_isUsed = node.x, node.y, node.isUsed

    if cx == N - 1 and cy == M - 1:
        print(answer[cx][cy])
        sys.exit(0)

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0 and not visited[nx][ny][c_isUsed]:
                visited[nx][ny][c_isUsed] = True
                queue.append(Node(nx, ny, c_isUsed))
                answer[nx][ny] = answer[cx][cy] + 1

            elif grid[nx][ny] == 1 and c_isUsed == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append(Node(nx, ny, 1))
                answer[nx][ny] = answer[cx][cy] + 1

print(-1)