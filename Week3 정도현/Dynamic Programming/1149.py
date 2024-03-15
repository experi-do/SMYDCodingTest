import sys
input = sys.stdin.readline
color = []

n = int(input())
for i in range(n):
    r, g, b = map(int, input().split(' '))
    color.append([r, g, b])

cost = [[0 for _ in range(3)] for _ in range(n)]
cost[0][0], cost[0][1], cost[0][2] = color[0][0], color[0][1], color[0][2]

for i in range(1, n):
    cost[i][0] = min(cost[i-1][1] + color[i][0], cost[i-1][2] + color[i][0])
    cost[i][1] = min(cost[i-1][0] + color[i][1], cost[i-1][2] + color[i][1])
    cost[i][2] = min(cost[i-1][0] + color[i][2], cost[i-1][1] + color[i][2])

print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))