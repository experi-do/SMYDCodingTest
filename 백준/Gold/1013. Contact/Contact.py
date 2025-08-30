import re

t = int(input())

for _ in range(t):
    sample = input()
    pred = re.compile("^(100+1+|01)+$")
    print("YES" if pred.match(sample) else "NO")