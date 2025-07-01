import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]

answer = [[n * m] * n for _ in range(m)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
row = m
col = n

answer[0][0] = 0
queue.append((0, 0))


def bfs():
    while queue:
        node_row, node_col = queue.popleft()

        for i in range(4):
            n_row = node_row + dx[i]
            n_col = node_col + dy[i]

            if 0 <= n_row < row and 0 <= n_col < col:
                cost = grid[n_row][n_col]
                new_cost = answer[node_row][node_col] + cost

                if answer[n_row][n_col] > new_cost:
                    answer[n_row][n_col] = new_cost
                    if cost == 0:
                        queue.appendleft((n_row, n_col))
                    else:
                        queue.append((n_row, n_col))


bfs()
print(answer[row - 1][col - 1])
