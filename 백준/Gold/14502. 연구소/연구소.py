import sys
input = sys.stdin.readline

import copy

from collections import deque

def bfs():
    global answer

    q = deque()
    safe = copy.deepcopy(map_list)

    for i in range(n):
        for j in range(m):
            if safe[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if safe[nx][ny] == 0:
                    safe[nx][ny] = 2
                    q.append([nx, ny])

    temp = 0
    for i in range(n):
        temp += safe[i].count(0)

    answer = max(answer, temp)

def wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if map_list[i][j] == 0:
                map_list[i][j] = 1
                wall(count+1)
                map_list[i][j] = 0

n, m = map(int, input().split())
answer = 0
map_list = [list(map(int,input().split())) for _ in range(n)]

wall(0)
print(answer)