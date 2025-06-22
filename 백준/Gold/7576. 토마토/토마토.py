'''
1. Stack
- 스택에 있는 좌표들을 pull하여 처리하고 이웃을 새로운 스택에 push
- 현재 stack이 비면 전파 횟수 +1
2. 처리한 0의 개수를 count
- 1 이상이면 계속 진행
- 0 이면
    - 전체 0의 개수와 같으면 최종 전파 횟수를 출력하고 종료
    - 다르면 -1 출력하고 종료
3.
'''
import sys
input = sys.stdin.readline()

n, m = map(int, input.split(' '))
grid = []
for _ in range(m):
    input = sys.stdin.readline()
    l = list(map(int, input.split(' ')))
    grid.append(l)

visited = [[False for _ in range(n)] for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zero = 0
blank = 0
stack = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            zero += 1
        elif grid[i][j] == -1:
            blank += 1
            visited[i][j] = True
        elif grid[i][j] == 1:
            stack.append([i, j])
            visited[i][j] = True

ans = 1
zero_counter = 0
while True:
    if len(stack)==0:
        if zero_counter == zero:
            print(ans-2) #1부터 시작했으므로
        else:
            print(-1)
        break
    new_stack = []
    ans += 1
    while stack:
        node = stack.pop()
        cx = node[0]
        cy = node[1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            grid[nx][ny] += ans
            visited[nx][ny] = True
            new_stack.append([nx, ny])
            zero_counter += 1
    stack = new_stack.copy()