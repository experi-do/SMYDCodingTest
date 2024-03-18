import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
record = list(map(int, input().split(' ')))

left, right = min(record), 1e9
answer = 0

while left < right:

    mid = (left + right) // 2
    sum = 0
    cnt = 0
    for i in range(n):
        if sum + record[i] > mid:
           cnt += 1
           sum = 0
        sum += record[i]

    if sum:
        cnt += 1

    if cnt > m:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(int(answer))