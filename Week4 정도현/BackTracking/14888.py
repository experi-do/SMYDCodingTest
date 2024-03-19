import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
nums = list(map(int, input().split(' ')))
calc = list(map(int, input().split(' ')))
calc_cnt = []

cnt = 0
for i in calc:
    for j in range(i):
        calc_cnt.append(cnt)
    cnt += 1
#print(calc_cnt)

answer = []
stack = []
visited = [False]*(n-1)

def dfs():
    if len(stack) == n-1:
        ans = nums[0]
        for k in range(n-1):
            ans = calculation(ans, nums[k+1], calc_cnt[stack[k]])
            #print('기호: ', stack[k])
        answer.append(ans)
        #print('answer: ', answer)
        #print('stack: ', stack)

    for i in range(n-1):
        if visited[i] == True:
            continue

        stack.append(i)
        visited[i] = True

        dfs()

        stack.pop()
        visited[i] = False

def calculation(a:int, b:int, sth: int):
    if sth == 0:
        ans = a+b
    elif sth == 1:
        ans = a-b
    elif sth == 2:
        ans = a*b
    else:
        if a < 0 and a % b != 0:
            ans = a // b + 1
        else:
            ans = a // b
    #print(a, b, sth)
    #print('ans: ', ans)
    return ans


dfs()
#print('min: ', min(answer))
#print('max: ', max(answer))
print(max(answer))
print(min(answer))
