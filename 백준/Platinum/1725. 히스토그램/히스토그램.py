import sys

n = int(sys.stdin.readline())
blocks = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
max_area = 0

for i in range(n + 1):
    height = blocks[i] if i < n else 0

    while stack and blocks[stack[-1]] >= height:
        h = blocks[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, h * width)

    stack.append(i)

print(max_area)