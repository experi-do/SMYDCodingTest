import sys
import math

input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

ans_list = []
# 총감독관 + 부감독관: a[i] < b + c*x -> 1 + x
# 총감독관: a[i] < b -> 1
# 2가지 경우에서 min

def get_t(student):
    left = student - b
    if (left <= 0):
        return 1
    else:
        return 1 + math.ceil(left / c)

ans = 0
for student in a_list:
    ans += get_t(student)
print(ans)