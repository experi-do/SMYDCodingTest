import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
triangle = defaultdict(list)
for i in range(n):
    val = list(map(int, input().split(' ')))
    triangle[i].append(val)


#dp[i] = curr + max(dp[i-1], dp[i])

def dp_func():
    dp = triangle[0][0]
    for k in range(n-1):
        temp = []
        for i in range(len(dp)+1):
            curr = triangle[k+1][0][i]
            if (i-1) < 0:
                prev = dp[i]
            elif (i >= len(dp)):
                prev = dp[i-1]
            else:
                prev = max(dp[i-1], dp[i])
            temp.append(curr + prev)
        dp = temp.copy()
    print(max(dp))


dp_func()