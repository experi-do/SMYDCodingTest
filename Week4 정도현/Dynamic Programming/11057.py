import sys
input = sys.stdin.readline

n = int(input())

dp = [[1 for _ in range(10)]]

for i in range(1, n):
    temp = []
    for j in range(10):
        sum = 0
        for k in range(j+1):
            sum += dp[i-1][k]
        temp.append(sum)
    dp.append(temp)

answer = 0
for i in range(10):
    answer += dp[n-1][i]
print(answer%10007)