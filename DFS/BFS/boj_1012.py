import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0 , 1, 0]

for i in range(T):
    M, N, K = map(int,input().split())
    graph = [[0]*(N) for _ in range(M)]
    visited = [[False] *(N) for _ in range(M)]

    for i in range(K):
        r, c = map(int,input().split())
        graph[r][c] = 1
    
    # 지렁이 개수
    count = 0

    def bfs(r, c):
        queue = deque()
        queue.append([r,c]) 
        graph[r][c] = 0
        visited[r][c] = True 
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                now_x = x + dx[i]
                now_y = y + dy[i]
                if now_x >= 0 and now_x < M and now_y >= 0 and now_y < N:
                    if graph[now_x][now_y]  == 1 and visited[now_x][now_y] == False :
                        visited[now_x][now_y] = True
                        graph[now_x][now_y] = 0
                        queue.append((now_x,now_y))
                    

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
