import sys
input = sys.stdin.readline

t, total = map(int, input().split(' '))
trees = sorted(list(map(int, input().split(' '))))

start = 0
end = trees[-1]
answer = 0
while start <= end:

    mid = (start + end) // 2

    add = 0
    for i in trees:
        if (i - mid) > 0:
            add += (i - mid)

    if add > total: # H를 높여야 함.
        answer = mid
        start = mid + 1
    elif add < total:
        end = mid - 1
    else:
        answer = mid
        break

print(answer)