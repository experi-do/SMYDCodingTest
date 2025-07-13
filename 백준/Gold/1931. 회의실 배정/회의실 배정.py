import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

# 종료 시간 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = meetings[0][1]

for meet in meetings[1:]:
    if meet[0] < end:
        continue
    cnt += 1
    end = meet[1]

print(cnt)