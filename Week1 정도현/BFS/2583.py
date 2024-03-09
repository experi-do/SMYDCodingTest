from typing import List
from collections import deque

class Solution2583:

    grid: [List[List[str]]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt_list = []

    def bfs(self, i: int, j: int):
        q = deque()
        q.append([i,j])
        self.grid[i][j] = '0'

        count = 1
        while q:
            v = q.popleft()

            for k in range(4):
                nx = v[0] + self.dx[k]
                ny = v[1] + self.dy[k]

                if (0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0])):
                    if (self.grid[nx][ny] == '1'):
                        q.append([nx, ny])
                        self.grid[nx][ny] = '0'
                        count += 1

        self.cnt_list.append(count)

    def count_area(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (self.grid[i][j] == '1'):
                    self.bfs(i, j)
                    count += 1

        return count

m, n, k = map(int, input().split(' '))

grid = [['1' for _ in range(n)] for _ in range(m)]

for t in range(k):
    x1, y1, x2, y2 = map(int, input().split(' '))

    left = [m-y1, x1]
    right = [m-y2, x2]

    for x in range(right[0], left[0]):
        for y in range(left[1], right[1]):
            grid[x][y] = '0'

solution = Solution2583()
solution.grid = grid
print(solution.count_area())

result = sorted(solution.cnt_list)
for ans in result:
    print(ans, end=' ')



