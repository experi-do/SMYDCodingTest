import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
wine = []
for i in range(n):
    price = int(input())
    wine.append(price)

cnt = [0]*n

cnt[0] = wine[0]
if n > 1:
    cnt[1] = wine[0]+wine[1]

if n > 2:
    cnt[2] = max(wine[2]+wine[1], wine[2]+wine[0], cnt[1])

for i in range(3, n):
    cnt[i] = max(cnt[i-1], cnt[i-3]+wine[i-1]+wine[i], cnt[i-2]+wine[i])

print(cnt[n-1])