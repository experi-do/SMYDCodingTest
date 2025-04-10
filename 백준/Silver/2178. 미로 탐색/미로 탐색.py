'''
    처음부터 끝까지 이동할 때 지나야 하는 노드 수를 구하는 문제
'''

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append([0, 0])
visited[0][0] = True
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1 and visited[ny][nx] == False:
            visited[ny][nx] = True
            queue.append([ny, nx])
            grid[ny][nx] = grid[y][x] + 1

print(grid[n-1][m-1])