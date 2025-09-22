t = int(input())

for _ in range(t):
    n = int(input())

    '''
    <1>
    1
    <2>
    1+1, 2
    <3>
    1+1+1, 2+1, 3
    <4>
    1+1+1+1, 2+1+1, 2+2, 3+1
    <5>
    1+1+1+1+1, 2+1+1+1, 2+2+1, 2+3, 3+1+1, 3+2
    
    '''

    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, 4):
        for j in range(i, n+1):
            dp[j] += dp[j-i]

    print(dp[n])