import sys

r, c, k = map(int, input().split())
grid = []
for _ in range(3):
        grid.append(list(map(int, input().split())))

# print(grid)

def run_R():
    new_grid = []
    for i in range(len(grid)):
        keys = tuple(set(grid[i]))
        temp = []
        for key in keys:
            if key != 0:
                temp.append([key, grid[i].count(key)])
        temp.sort(key=lambda x:(x[1], x[0]))
        new_grid.append(sum(temp, [])) # lesson learned

    max_length = max(len(row) for row in new_grid)
    for row in new_grid:
        while len(row) < max_length:
            row.append(0)
    # print(new_grid)
    return new_grid

def tranpose(grid):
    return list(map(list, zip(*grid)))

def run_C():
    tranpose_grid = tranpose(grid)
    # print('here:', tranpose_grid)
    new_grid = []
    for i in range(len(tranpose_grid)):
        keys = tuple(set(tranpose_grid[i]))
        temp = []
        for key in keys:
            if key != 0:
                temp.append([key, tranpose_grid[i].count(key)])
        temp.sort(key=lambda x: (x[1], x[0]))
        new_grid.append(sum(temp, []))  # lesson learned

    max_length = max(len(row) for row in new_grid)
    for row in new_grid:
        while len(row) < max_length:
            row.append(0)
    # print('here2: ', new_grid)
    new_grid = tranpose(new_grid)
    # print(new_grid)
    return new_grid


answer = 0
while True:
    if len(grid) >= r and len(grid[0]) >= c:
        if grid[r-1][c-1] == k:
            break

    if answer > 100:
        answer = -1
        break

    answer += 1

    len_r, len_c = len(grid), len(grid[0])

    if len_r >= len_c:
        # print('R')
        new_grid = run_R()
        grid = new_grid.copy()
    else:
        # print('C')
        new_grid = run_C()
        grid = new_grid.copy()


if answer > 100:
    print(-1)
else:
    print(answer)