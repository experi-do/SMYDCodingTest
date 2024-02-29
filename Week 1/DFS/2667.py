from typing import List
import sys
sys.setrecursionlimit(10**5)

class Solution2667:
    grid: List[List[str]]

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

    def sizeTown(self):
        if not self.grid:
            return 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    self.cnt_list.append(self.count)
                    self.count = 0

        self.cnt_list.sort()
        return self.cnt_list

n = int(input())
grid = []
for _ in range(n):
    data = input()
    grid.append([c for c in data])

solution = Solution2667()
solution.grid = grid
solution.sizeTown()
print(len(solution.cnt_list))
for i in range(len(solution.cnt_list)):
    print(solution.cnt_list[i])
