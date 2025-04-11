import sys

input = sys.stdin.readline

n = int(input())
time = []
price = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if (i + time[i] <= n):
        dp[i] = max(dp[i + time[i]] + price[i], dp[i+1]) # 상담을 했으니까 비용 추가
    else:
        dp[i] = dp[i+1] # 상담을 하지 않는 경우

print(dp[0])