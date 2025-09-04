import sys

n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

def getLength(start, dir):
    cnt = 0
    while True:
        # print(f'[0]: {start[0] + dir[0]} [1]: {start[1] + dir[1]}')
        if (0 <= start[0] + dir[0] < n and 0 <= start[1] + dir[1] < n and grid[start[0] + dir[0]][start[1] + dir[1]] == 1):
            cnt += 1
        else:
            break
        start = start[0] + dir[0], start[1] + dir[1]
    return start, cnt


headFlag = True
headPos = None
for i in range(n):
    temp = sys.stdin.readline().strip()
    for j in range(n):
        if temp[j] == '*':
            grid[i][j] = 1
            if headFlag:
                headPos = (i, j)
                headFlag = False

heartPos = (headPos[0]+1, headPos[1])

# print(grid)

len_list = []
len_list.append(getLength(heartPos, (0, -1)))
len_list.append(getLength(heartPos, (0, 1)))
len_list.append(getLength(heartPos, (1, 0)))

legPos = len_list[-1][0]
# print(f'legPos: {legPos}')
left_leg = getLength((legPos[0]+1, legPos[1]-1), (1, 0))
right_leg = getLength((legPos[0]+1, legPos[1]+1), (1, 0))

len_list.append((left_leg[0], left_leg[1]+1))
len_list.append((right_leg[0], right_leg[1]+1))

print(heartPos[0]+1, heartPos[1]+1)
for l in len_list:
    print(l[1], end=' ')