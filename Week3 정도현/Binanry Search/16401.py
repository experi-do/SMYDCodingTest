from typing import List
import sys
input = sys.stdin.readline

m, n = map(int, input().split(' '))
snack = sorted(list(map(int, input().split(' '))))

class Solution16401:

    lst: List[int]
    m: int
    n: int

    def binary_search(self):
        start = 1
        end = max(self.lst)

        answer = 0
        while start <= end:

            mid = (start + end) // 2

            cnt = 0
            for i in self.lst:
                cnt += i // mid

            if cnt >= self.m: # mid값을 더 키워도 된다는 뜻
                answer = mid
                start = mid + 1
            else: # mid값을 작게 해야 한다는 뜻
                end = mid -1
        return answer

solution = Solution16401()
solution.lst = snack
solution.m = m
solution.n = n

print(solution.binary_search())


