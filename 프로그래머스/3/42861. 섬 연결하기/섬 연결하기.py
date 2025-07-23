import heapq
from collections import defaultdict

def solution(n, costs):
    answer = 0
    
    grid = defaultdict(list)
    visited = [False] * (n+1)
    for cost in costs:
        a, b, w = cost[0], cost[1], cost[2]
        grid[a].append((w, b)) # (cost, neighbor)
        grid[b].append((w, a))
    
    q = grid[0]
    heapq.heapify(q)
    visited[0] = True
    mst = [0]
    answer = 0
    while q:
        c, next = heapq.heappop(q)
        if visited[next] == False:
            visited[next] = True
            mst.append(next)
            answer += c
            
            for neighbor in grid[next]:
                if visited[neighbor[1]] == False:
                    heapq.heappush(q, (neighbor))
    
        
    return answer