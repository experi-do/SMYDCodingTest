# 높은 자릿수부터 탐색하면서 현재 자릿수가 이전 자릿수보다 크면 이전 자릿수는 pass

import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
num = input()
num = [int(num[i]) for i in range(n)]
stack = [num[0]]

for i in range(1, len(num)):

    while len(stack) > 0 and k > 0:
        if stack[-1] < num[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num[i])

if k > 0:
    print(''.join(map(str, stack[:-k])))
else:
    print(''.join(map(str, stack)))