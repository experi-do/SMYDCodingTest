n = int(input())
ans = 0

memo = [0]*(1001)
memo[1] = 1
memo[2] = 2
for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]
print(memo[n]%10007)