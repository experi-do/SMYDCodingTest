import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
c_list = input()
num_list = []
for i in range(len(c_list)-1):
    num_list.append(int(c_list[i]))
print(num_list)