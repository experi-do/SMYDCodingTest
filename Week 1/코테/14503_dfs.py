from typing import List
import sys

class Solution14503:
    grid: [List[List[str]]]
    count = 0

    def dfs(self, i:int, j:int):
        if (
            i < 0 or i >= len(self.grid) or
            j < 0 or j >= len(self.grid) or
            self.grid[i][j] != '1'
        ):
            return

        self.grid[i][j] == '0'

        self.dfs(i-1, j)
        self.dfs(i+1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)
        self.dfs(i-1, j+1)
        self.dfs(i-1, j-1)
        self.dfs(i+1, j+1)
        self.dfs(i+1, j-1)

    def countLetter(self):
        print(len(self.grid))
        print(len(self.grid[0]))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (self.grid[i][j] == '1'):
                    self.dfs(i, j)
                    self.count += 1
                    print('here')
        return self.count



m, n = map(int, input().split(' '))
grid = []

print(m, n)

for i in range(m):
    small_grid = input().split(' ')
    grid.append(small_grid)

solution = Solution14503()
solution.grid = grid
print(solution.grid)
result = solution.countLetter()
print(result)