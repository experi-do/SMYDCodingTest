from typing import List
import sys
sys.setrecursionlimit(10**5)

class Solution14503:

    grid: [List[List[str]]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def robot(self, i: int, j:int, dir: int):
        cnt_2 = 0
        # 현재 칸을 청소(2)로 표시
        if (self.grid[i][j] != '2'):
            self.grid[i][j] = '2'
            cnt_2 += 1
        count = 0
        for k in range(4):
            nx = i + self.dx[k]
            ny = j + self.dy[k]

            if (self.grid[nx][ny] == '0'):
                count += 1


        # 주변이 모두 청소 완료
        if (count == 0):
            if (dir == 0):
                if (self.grid[i + 1][j] == '1'):
                    dir = -1
                i = i + 1
            elif (dir == 1):
                if (self.grid[i][j - 1] == '1'):
                    dir = -1
                j = j - 1
            elif (dir == 2):
                if (self.grid[i - 1][j] == '1'):
                    dir = -1
                i = i - 1
            else:
                if (self.grid[i][j + 1] == '1'):
                    dir = -1
                j = j + 1
            return [i, j, dir, cnt_2]
        else:
            if (dir == 0):
                dir = 3
                if (self.grid[i][j - 1] == '0'):
                    j = j - 1
            elif (dir == 1):
                dir = 0
                if (self.grid[i - 1][j] == '0'):
                    i = i - 1
            elif (dir == 2):
                dir = 1
                if (self.grid[i][j + 1] == '0'):
                    j = j + 1
            else:
                dir = 2
                if (self.grid[i + 1][j] == '0'):
                    i = i + 1
            return [i, j, dir, cnt_2]


n, m = map(int, input().split(' '))
i, j, dir = map(int, input().split(' '))
cnt = 0
grid = []
for _ in range(n):
    grid.append(input().split(' '))

solution = Solution14503()
solution.grid = grid
while (dir != -1):
    i, j, dir, plus = solution.robot(i, j, dir)
    cnt = cnt + plus

print(cnt)



