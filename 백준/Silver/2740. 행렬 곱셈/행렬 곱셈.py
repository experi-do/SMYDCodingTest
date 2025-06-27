import sys

matA = []
matB = []

input = sys.stdin.readline()
n, m = map(int, input.split())

for _ in range(n):
    input = sys.stdin.readline()
    matA.append(list(map(int, input.split())))

input = sys.stdin.readline()
n, m = map(int, input.split())
for _ in range(n):
    input = sys.stdin.readline()
    matB.append(list(map(int, input.split())))


for i in range(len(matA)):
    for j in range(len(matB[0])):
        ans = 0
        for k in range(len(matA[0])):
            ans += matA[i][k] * matB[k][j]
        print(ans, end=' ')
    print()