from collections import deque


def solution(maps):

    n = len(maps)
    m = len(maps[0])

    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([[0, 0]])
    visited[0][0] = 1

    # BFS
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if (visited[nx][ny] == False) and (maps[nx][ny] == 1):
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return -1