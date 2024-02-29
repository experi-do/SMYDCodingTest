from typing import List
import sys
#sys.setrecursionlimit(10**5)
class Solution1743:

    grid : List[List[str]]

    count = 0
    cnt_list = []

    def dfs(self, i: int, j: int):
        if (i < 0 or i >= len(self.grid) or
            j < 0 or j >= len(self.grid[0]) or
            self.grid[i][j] != '1'):
            return
        else:
            self.count += 1

        self.grid[i][j] = '0'

        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)

    def sizeTrash(self):
        if not self.grid:
            return 0
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    self.cnt_list.append(self.count)
                    self.count = 0
        return max(self.cnt_list)


h, w, n = map(int, input().split(' '))

grid = [['0' for _ in range(w)] for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split(' '))
    grid[a-1][b-1] = '1'

solution = Solution1743()
solution.grid = grid
print(solution.sizeTrash())

