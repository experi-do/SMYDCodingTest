import sys
input = sys.stdin.readline

n = int(input().strip())
min_p, min_f, min_s, min_v = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# grid[i] = [p, f, s, v, cost]

best_cost = float('inf')
best_pick = None

def dfs(start, p, f, s, v, cost, pick):
    global best_cost, best_pick

    if cost >= best_cost:
        return

    if p >= min_p and f >= min_f and s >= min_s and v >= min_v:
        if cost < best_cost:
            best_cost = cost
            best_pick = pick[:]
        elif cost == best_cost:
            if best_pick is None or pick < best_pick:
                best_pick = pick[:]
        return
        
    for i in range(start, n):
        pi, fi, si, vi, ci = grid[i]
        dfs(i + 1, p + pi, f + fi, s + si, v + vi, cost + ci, pick + [i])

dfs(0, 0, 0, 0, 0, 0, [])

if best_cost == float('inf'):
    print(-1)
else:
    print(best_cost)
    print(*[x+1 for x in best_pick])

