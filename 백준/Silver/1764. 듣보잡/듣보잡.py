import sys

n, m = map(int, input().split())
listen = set()
for _ in range(n):
    listen.add(sys.stdin.readline().strip())
look = set()
for _ in range(m):
    look.add(sys.stdin.readline().strip())

answer = sorted(list(listen & look))

print(len(answer))
for name in answer:
    print(name)
