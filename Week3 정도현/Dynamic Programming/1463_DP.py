import sys
input = sys.stdin.readline

n = int(input())

d_list = [0]*(n+1)
def dp(n:int):
    d_list[1] = 0
    for i in range(2, n+1):
        d_list[i] = (d_list[i-1] + 1)
        if (i % 3 == 0):
            d_list[i] = min(d_list[i], d_list[i//3]+1)
        if (i % 2 == 0):
            d_list[i] = min(d_list[i], d_list[i//2]+1)
    print(d_list[n])

dp(n)
