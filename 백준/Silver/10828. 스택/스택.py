from collections import deque
import sys

n = int(input())
cmd_list = deque()
for i in range(n):
    input = sys.stdin.readline()
    cmd = input.split()
    cmd_list.append(cmd)

stack = []
for i in range(n):
    cmd = cmd_list.popleft()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)