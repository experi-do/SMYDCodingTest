from collections import defaultdict
import sys, math

grid = []
for _ in range(10):
    grid.append(list(map(int, sys.stdin.readline().split())))
visited = [[False for _ in range(10)] for _ in range(10)]
use = defaultdict(int)
for i in range(1, 6):
    use[i] = 0

answer = math.inf

def can_attach(x, y, size):
    if (x + size > 10) or (y + size > 10):
        # print(f'can attach? False1')
        return False
    for i in range(x, x+size):
        for j in range(y, y+size):
            # print(f'i: {i}, j: {j}, grid[i][j]: {grid[i][j]}, visited[i][j]: {visited[i][j]}')
            if grid[i][j] == 0 or visited[i][j] == True:
                return False
    # print(f'can attach? True')
    return True


def attach(x, y, size, value):
    for i in range(x, x+size):
        for j in range(y, y+size):
            visited[i][j] = value


def dfs(x, y, count):
    global answer
    # print(f'x: {x}, y: {y}, count: {count}')
    if (x >= 10):
        # print(f'answer: {answer}, count: {count}')
        answer = min(answer, count)
        return

    if (y >= 10):
        dfs(x + 1, 0, count)
        return

    if (visited[x][y] == True or grid[x][y] == 0):
        dfs(x, y + 1, count)
        return

    for size in [5, 4, 3, 2, 1]:
        if (use[size] >= 5 or not can_attach(x, y, size)):
            # print(f'{size} has continued')
            continue
        attach(x, y, size, True)
        # print(f'size {size} appended for {x}, {y}')
        use[size] += 1
        # print(f'current use: {use}')

        dfs(x, y + 1, count + 1)

        use[size] -= 1
        attach(x, y, size, False)


def solve():
    dfs(0, 0, 0)
    print(-1 if answer == math.inf else answer)


solve()
# import sys
# from collections import defaultdict
#
# def check(row, col, length):
#     print(f'current length: {length}')
#     isTrue = True
#     for i in range(row, row + length):
#         if (row + length > 10):
#             return False
#         if isTrue == False:
#             break
#         for j in range(col, col + length):
#             if (col + length > 10):
#                 return False
#             print(f'[check] i: {i}, j: {j}')
#             print(f'grid[i][j]: {grid[i][j]}')
#             if grid[i][j] == 0 or visited[i][j] == True:
#                 isTrue = False
#                 break
#     return isTrue
#
# grid = []
# for _ in range(10):
#     grid.append(list(map(int, sys.stdin.readline().split())))
#
# use = defaultdict(int)
# for i in range(1, 6):
#     use[i] = 0
# # print(grid)
#
#
# visited = [[False for _ in range(10)] for _ in range(10)]
# for length in range(5, 0, -1):
#     iterFlag = True
#     for i in range(10):
#         if iterFlag == False:
#             break
#         for j in range(10):
#             if iterFlag == False:
#                 break
#             print(f'i: {i}, j: {j}, grid[i][j] = {grid[i][j]}, visited[i][j] = {visited[i][j]}')
#             if grid[i][j] == 1 and visited[i][j] == False:
#                 if use[length] >= 5:
#                     iterFlag = False
#                 else:
#                     isTrue = check(i, j, length)
#                     if isTrue:
#                         print(f'i: {i}, j: {j}, length: {length}, isTrue: {isTrue}')
#                         print(use)
#                         use[length] += 1
#                         for r in range(i, i+length):
#                             for c in range(j, j+length):
#                                 visited[r][c] = True
#
# def getAnswer(visited, grid):
#     for i in range(10):
#         for j in range(10):
#             if grid[i][j] == 1 and visited[i][j] == False:
#                 return -1
#     answer = 0
#     for key in use.keys():
#         answer += use[key]
#     print(use)
#     return answer
#
# print(getAnswer(visited, grid))