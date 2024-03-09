# 양방향 주의

import sys
input = sys.stdin.readline

from collections import defaultdict

class Solution2606:

    graph: defaultdict(list)
    connected = 0

    def dfs(self, i: int, discovered=[]):

        discovered.append(i)

        for node in self.graph[i]:
            if node not in discovered:
                self.connected += 1
                discovered = self.dfs(node)
                discovered.append(node)
        return discovered



com = int(input())
pairs = int(input())
connections = defaultdict(list)

for _ in range(pairs):
    a, b = map(int, input().split(' '))
    connections[a].append(b)
    connections[b].append(a)

solution = Solution2606()
solution.graph = connections
solution.dfs(1)
print(solution.connected)