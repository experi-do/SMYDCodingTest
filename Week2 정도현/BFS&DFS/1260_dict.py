from collections import deque
import sys
input = sys.stdin.readline

from collections import defaultdict

class Solutioin1260:

    node_dict = defaultdict(list)

    def dfs(self, i: int, discovered = []):
        discovered.append(i)
        for v in self.node_dict[i]:
            if v not in discovered:
                discovered = self.dfs(v, discovered)
        return discovered

    def bfs(self, i: int):
        q = deque([i])
        discovered = [i]
        while q:
            v = q.popleft()
            for w in self.node_dict[v]:
                if w not in discovered:
                    q.append(w)
                    discovered.append(w)
        return discovered


n, m, v = map(int, input().split(' '))
temp_dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split(' '))
    temp_dict[a].append(b)
    temp_dict[b].append(a)

for key in temp_dict:
    temp_dict[key] = sorted(temp_dict[key])

solution = Solutioin1260()
solution.node_dict = temp_dict
discovered = []
dfs = solution.dfs(v)
bfs = solution.bfs(v)

for d in dfs:
    print(d, end = ' ')
print()
for b in bfs:
    print(b, end = ' ')
