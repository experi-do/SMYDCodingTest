import sys
sys.stdin.readline

n, l = map(int, input().split(' '))

blank = list(map(int, input().split(' ')))

blank.sort()

tape_cnt = 1
start = blank[0]
for i in range(1,n):
    if blank[i] in range(start, start+l):
        continue
    tape_cnt += 1
    start = blank[i]
print(tape_cnt)