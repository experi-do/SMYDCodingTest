'''
오1 오2 오1 오1 오2
아2 위1 위2 아2 위1

오2오2오1오1오1
위1위1위2아2아2

(-2, +1)
(-1, +2)
(-2, -1)
(-1, -2)
(+1, +2)
(+2, +1)
(+1, -2)
(+2, -1)
'''
from collections import deque

t = int(input())

dx = [-2, -1, -2, -1, 1, 2, 1, 2]
dy = [1, 2, -1, -2, 2, 1,-2,-1]

for _ in range(t):
    I = int(input())
    init_x, init_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    queue = deque()
    visited = [[0 for _ in range(I)] for _ in range(I)]
    queue.append((init_x, init_y, visited[0][0]))
    visited[init_x][init_y] = 1

    while queue:
        node = queue.popleft()
        cx, cy, cnt = node[0], node[1], node[2]
        if cx == target_x and cy == target_y:
            print(visited[target_x][target_y]-1)
            break
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny, visited[nx][ny]))