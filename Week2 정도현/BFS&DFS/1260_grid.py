n, m, v = map(int, input().split(' '))

grid = [['0' for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split(' '))
    grid[a][b] = grid[b][a] = '1'

dfs_visit = [0]*(n+1)
bfs_visit = [0]*(n+1)

def dfs(node):
    dfs_visit[node] = 1
    print(node, end = ' ')
    for i in range(1, n+1):
        if grid[node][i] == '1' and dfs_visit[i] == 0:
            dfs(i)

def bfs(node):
    q = [node]
    bfs_visit[node] = 1
    while q:
        node = q.pop(0)
        print(node, end=' ')
        for i in range(1, n+1):
            if(grid[node][i] == '1' and bfs_visit[i] == 0):
                q.append(i)
                bfs_visit[i] = 1

dfs(v)
print()
bfs(v)