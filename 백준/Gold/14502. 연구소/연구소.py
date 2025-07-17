import sys, math
from itertools import combinations

'''
세균 dfs -> max count == min safety zone
'''

N, M = map(int, sys.stdin.readline().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

blank = []
virus = []
wall = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            blank.append((i, j))
        elif grid[i][j] == 2:
            virus.append((i, j))
        else:
            wall.append((i, j))

blank_comb = combinations(blank, 3)

def dfs():

    visited = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    virus_zone = 0
    for v in virus:
        x, y = v
        stack =[(x, y)]
        visited[x][y] = True
        cnt = 0
        while stack:
            cx, cy = stack.pop()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and visited[nx][ny] == False and grid[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
        virus_zone += cnt
    return virus_zone



answer = N*M
for comb in blank_comb:
    # 벽 3개 추가
    new_grid = grid.copy()
    for node in comb:
        x, y = node
        grid[x][y] = 1
    virus_zone = dfs()
    answer = min(answer, virus_zone)
    for node in comb:
        x, y = node
        grid[x][y] = 0

wall_node = len(wall) + 3
virus_node = len(virus) + answer
print(N*M - (wall_node + virus_node))