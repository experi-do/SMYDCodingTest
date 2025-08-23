N = int(input())
M = int(input())

arr = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    arr[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()