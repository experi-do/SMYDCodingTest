# 높은 자릿수부터 탐색하면서 현재 자릿수가 이전 자릿수보다 크면 이전 자릿수는 pass

import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
num = list(map(int, input().split(' ')))

result=[0 for _ in range(n-k)]
cnt = 0
for i in range(num):
