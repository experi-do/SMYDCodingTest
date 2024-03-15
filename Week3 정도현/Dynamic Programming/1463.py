import sys
input = sys.stdin.readline
from collections import deque
class Solution1463:

    def dp(self, n: int):
        q = deque()
        q.append((n,0))

        while q:
            num, idx = q.popleft()
            if num == 1:
                return idx

            if (num % 3 == 0):
                q.append((num // 3, idx + 1))
            if (num % 2 == 0):
                q.append((num // 2, idx + 1))
            q.append((num - 1, idx + 1))

solution = Solution1463()
N = int(input())
print(solution.dp(N))