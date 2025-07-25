import sys
N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [False] * N

def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            ans = min(ans, value)
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = True
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(ans)