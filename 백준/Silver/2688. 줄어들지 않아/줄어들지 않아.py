import sys, math

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(math.comb(n+9, 9))