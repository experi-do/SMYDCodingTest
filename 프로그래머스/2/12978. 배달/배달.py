from collections import defaultdict
import heapq
import math

def solution(N, road, K):
    answer = 0
    
    distance = [math.inf] * (N+1)
    distance[1] = 0
    
    grid = defaultdict(list)
    for info in road:
        a,b,c = info[0], info[1], info[2]
        grid[a].append((b,c))
        grid[b].append((a,c))
    
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cost, now = heapq.heappop(q)
        
        if distance[now] < cost:
            continue
        
        for next in grid[now]:
            if cost + next[1] < distance[next[0]]:
                distance[next[0]] = cost + next[1]
                heapq.heappush(q, (cost + next[1], next[0]))
    
    for d in distance:
        if d <= K:
            answer += 1
    return answer