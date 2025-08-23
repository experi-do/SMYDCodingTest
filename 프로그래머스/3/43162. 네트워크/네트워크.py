from collections import defaultdict, deque

def solution(n, computers):
    answer = 0
    
    net_dict = defaultdict(list)
    visited = [False for _ in range(n)]
    
    for idx, com in enumerate(computers):
        for i in range(len(com)):
            if i != idx and com[i] == 1:
                net_dict[idx].append(i)
                
    for i in range(n):
        if visited[i]:
            continue
            
        queue = deque([i])
        visited[i] = True
    
        while queue:
            c_node = queue.pop()

            next_nodes = net_dict[c_node]
            for n in next_nodes:
                if visited[n] == False:
                    queue.append(n)
                    visited[n] = True

        answer += 1
        
        
                
    return answer