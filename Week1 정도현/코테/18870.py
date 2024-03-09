import sys
input = sys.stdin.readline

n = int(input())
lst = input().split(' ')
num_lst = []
for num in lst:
    num = int(num)
    num_lst.append(num)

sorted_lst = sorted(list(set(sorted(num_lst))))

dict = {}
for i in range(len(sorted_lst)):
    dict[sorted_lst[i]] = i

for i in range(n):
    print(dict[num_lst[i]], end=' ')
