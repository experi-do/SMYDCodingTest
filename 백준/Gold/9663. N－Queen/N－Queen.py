N = int(input())
visited= []
count = 0

def check(r, c):
    for j in range(len(visited)):
        if abs(j - r) == abs(visited[j] - c):
            return False
    return True


def dfs(r):
    global count

    if r == N:
        count += 1
        return

    for col in range(N):
        if col not in visited:
            if check(r, col):
                visited.append(col)
                dfs(r + 1)
                visited.pop()

dfs(0)
print(count)