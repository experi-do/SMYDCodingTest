#40분
import sys
sys.setrecursionlimit(10**5) #runtimeerror
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[0]*(M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

# graph 설정
for i in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1

global trash_size
trash_size = 0

def dfs(r, c):
    global trash_size
    if r < 0 or r > N or c < 0 or c > M:
        return 0
    if graph[r][c] == 1 and visited[r][c] == False :
        trash_size += 1
        visited[r][c] = True
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r,c+1)
        dfs(r,c-1)
        
        return 1
    return 0

answer = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if dfs(i,j) == 1:
            answer = max(answer, trash_size)
            trash_size = 0
            
print(answer)
