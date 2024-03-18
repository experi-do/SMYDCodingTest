import sys
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split(' ')))

cnt_list = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] > nums[i]:
            cnt_list[i] = max(cnt_list[i], cnt_list[j] + 1)
print(max(cnt_list))
