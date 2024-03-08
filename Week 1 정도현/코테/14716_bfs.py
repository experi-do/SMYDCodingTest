from typing import List
from collections import deque

class Solution14716:

    grid: [List[List[str]]]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    def bfs(self, i: int, j: int):

        q = deque()
        q.append([i, j])
        self.grid[i][j] = 0

        while q:
            v = q.popleft()
            self.grid[v[0]][v[1]] = '0'

            for k in range(8):
                nx = v[0] + self.dx[k]
                ny = v[1] + self.dy[k]

                if (0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0])):
                    if (grid[nx][ny] == '1'):
                        q.append([nx, ny])
                        self.grid[nx][ny] = '0'



    def letter_count(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if(self.grid[i][j] == '1'):
                    self.bfs(i, j)
                    count += 1

        return count


m, n = map(int, input().split(' '))
grid = []


for i in range(m):
    small_grid = input().split(' ')
    grid.append(small_grid)

solution = Solution14716()
solution.grid = grid
result = solution.letter_count()
print(result)

