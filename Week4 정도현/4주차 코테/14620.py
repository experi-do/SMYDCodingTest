import sys
input = sys.stdin.readline

n = int(input())

garden = []
for _ in range(n):
    cost_list = list(map(int, input().split(' ')))
    garden.append(cost_list)
#print(garden)

check = [[0 for _ in range(n)] for _ in range(n)]
cost_add = [[0 for _ in range(n)] for _ in range(n)]
#print(check)

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def cost_check(i:int, j:int):
    cost = 0
    ##print('i, j: ', i, j)
    #print('cost: ', cost)
    for k in range(5):
        nx = i+dx[k]
        ny = j+dy[k]
   #     print('nx, ny: ', nx, ny)

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            cost_add[i][j] = -1
  #          print('pass')
            return
        cost += garden[nx][ny]

 #       print('cost: ', cost)
    cost_add[i][j] = cost

min_cost = []
for i in range(n):
    for j in range(n):
        cost_check(i, j)
        if cost_add[i][j] != -1:
            min_cost.append((cost_add[i][j], i, j))
#print(cost_add)

min_cost = sorted(min_cost)

#print(min_cost[0][1], min_cost[0][2])
check[min_cost[0][1]][min_cost[0][2]] = 1
check[min_cost[0][1]+1][min_cost[0][2]] = 1
check[min_cost[0][1]-1][min_cost[0][2]] = 1
check[min_cost[0][1]][min_cost[0][2]+1] = 1
check[min_cost[0][1]][min_cost[0][2]-1] = 1

print(len(min_cost))

cnt = 0
answer = min_cost[0][0]
for i in range(1, len(min_cost)):
    #print(min_cost[i])
    flag = 0
    answer += min_cost[i][0]
    for k in range(5):
        nx = min_cost[i][1]+dx[k]
        ny = min_cost[i][2]+dy[k]
        #print('nx, ny: ', nx, ny)
        flag += 1
        if check[nx][ny] == 1:
            print('***************************pass: ', min_cost[i])
            #print(i, nx, ny)
            answer -= min_cost[i][0]
            flag -= 1
            break
        #print('here')
    if flag == 5:
        check[min_cost[i][1]][min_cost[i][2]] = 1
        for k in range(5):
            nx = min_cost[i][1] + dx[k]
            ny = min_cost[i][2] + dy[k]
            check[nx][ny] = 1
        print(check)
        print('cnt: ', cnt)
        cnt += 1
    if cnt == 2:
        print(answer)
        #print('here')
        #print(check)
        break