import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
cook = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split(' '))
    cook[i].append(a)
    cook[i].append(b)
visited = [False]*(n)
stack = []
#print(cook)

diff = []
sum_a, sum_b = cook[0][0], cook[0][1]
def dfs(sum_a, sum_b):
    #print('===', ' '.join(map(str, stack)),'===')
    for i in range(n):
        if len(stack) > 0 and i < stack[-1]:
            continue

        if visited[i] == True:
            continue

        a, b = cook[i][0], cook[i][1]
        if len(stack) == 0:
            diff.append(abs(a - b))

        stack.append(i)
        visited[i] = True

        if i > 0: #and abs((sum_a) - (sum_b)) > abs((sum_a*a) - (sum_b+b)):
          #  print(sum_a, '* ', a, '= ', sum_a * a)
            sum_a *= a
         #   print(sum_b, '+ ', b, ' = ', sum_b+b)
            sum_b += b
            diff.append(abs(sum_a - sum_b))

        #print('diff: ', diff)
        dfs(sum_a, sum_b)

        stack.pop()
        visited[i] = False
        #print(sum_a, '/', a, '= ', sum_a / a)
        sum_a /= a
        #print(sum_b, '-', b, ' = ', sum_b - b)
        sum_b -= b

dfs(sum_a, sum_b)
print(int(min(diff)))