T = int(input())

'''
1자릿수: 0~9 -> 10
2자릿수 -> 10 + 9 + ~ + 1 = 55
- 0: 1개 - 00
- 1: 2개 - 01, 11
- 2: 3개 - 02, 12, 22 
- 3: 4개 - 03, 13, 23, 33
~
- 9: 10개 - 09, 19, 29, 39, 49, 59, 69, 79, 89, 99

[i][0]: sum([i-1][0]~[i-1][9])
[i][1]: sum([i-1][1]~[i-1][9])


'''
for _ in range(T):
    n = int(input())
    if n==1:
        print(10)
        continue

    memo = [[0]*10 for _ in range(n)]

    for i in range(10):
        memo[0][i] = 1

    for i in range(1, n):
        for j in range(10):
            memo[i][j] = sum(memo[i-1][j:])

    print(sum(memo[n-1]))