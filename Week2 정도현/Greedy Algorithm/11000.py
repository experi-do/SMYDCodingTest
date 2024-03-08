# n = int(input())
# class_lst = []
# for _ in range(n):
#     s, t = map(int, input().split(' '))
#     class_lst.append([s, t])
#
# cnt = 0
# class_lst.sort(key = lambda x:x[0])
#
# while (len(class_lst) != 0):
#
#     s, t = class_lst[0][0], class_lst[0][1]
#     class_lst.pop(0)
#
#     for i in range(len(class_lst)):
#         if class_lst[i][0] >= t:
#
#             s = class_lst[i][0]
#             t = class_lst[i][1]
#             class_lst.remove([s, t])
#             break
#     cnt += 1
# print(cnt)

import heapq
import sys
input = sys.stdin.readline

n = int(input())
class_lst = []

for _ in range(n):
    class_lst.append(list(map(int, input().split(' '))))

class_lst.sort(key = lambda x:(x[0], x[1]))

heap = [class_lst[0][1]] # 끝나는 시간만 저장
for i in range(1, n):
    if heap[0] <= class_lst[i][0]: # 한 강의실에서 이어서 수업할 수 있는 경우
        heapq.heappop(heap)
    heapq.heappush(heap, class_lst[i][1])

# heap에는 최종적으로 각 강의실에서 마지막으로 수업하는 것만 남게 됨 == 강의실 개수

print(len(heap))