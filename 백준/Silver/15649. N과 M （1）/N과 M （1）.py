n, m = map(int, input().split(' '))
stack = []
visited = [False]*(n+1)
def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(1, n+1):
        if visited[i] == True:
            continue

        stack.append(i)
        visited[i] = True

        dfs()

        stack.pop()
        visited[i] = False

dfs()