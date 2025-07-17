import sys

T = int(input())

for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        score.append(list(map(int, sys.stdin.readline().split())))

    score.sort()

    cnt = 1
    min_interview = score[0][1]

    for i in range(1, N):
        if score[i][1] < min_interview:
            cnt += 1
            min_interview = score[i][1]

    print(cnt)
