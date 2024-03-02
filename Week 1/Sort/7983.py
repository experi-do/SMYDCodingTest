import sys
input = sys.stdin.readline

n = int(input())
hw_list = []

for _ in range(n):
    d, t = map(int, input().split(' '))
    hw_list.append([d, t])

hw_list.sort(key=lambda x:-x[1])

last = hw_list[0][1]

for hw in hw_list:
    last = min(hw[1], last) - hw[0]

print(last)