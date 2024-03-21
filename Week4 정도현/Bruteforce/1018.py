import sys
input = sys.stdin.readline

m, n = map(int, input().split(' '))

map = []
for _ in range(m):
    row = input()
    temp = []
    for i in range(len(row)-1):
        temp.append(row[i])
    map.append(temp)

chess = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

def count(a: int, b: int):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (chess[i][j] == map[a+i][b+j]):
                cnt += 1
    return min(cnt, 64 - cnt)

answer = m*n
for i in range(m-7):
    for j in range(n-7):
        answer = min(answer, count(i, j))
print(answer)
