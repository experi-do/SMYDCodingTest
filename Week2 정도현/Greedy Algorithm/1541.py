# 아이디어: '-'가 나오면 괄호 그 뒤로 모두 빼면 됨 == -값을 최대한 크게 만들기
from typing import List

class Solution1541:
    calc: [List[str]]
    plus_value = 0
    minus_value = 0

    def find_nums(self):
        nums = []
        signs = ['+']
        current_num = ''

        for char in self.calc:
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    nums.append(int(current_num))
                    current_num = ''
                if (char == '+' or char == '-'):
                    signs.append(char)

        if current_num: # 마지막 숫자가 남아있는 경우
            nums.append(int(current_num))

        return nums, signs

    def check_minus(self):
        nums, signs = self.find_nums()

        plus_value = 0
        minus_value = 0

        check = False
        for i in range(len(nums)):
            if (signs[i] == '-'):
                check = True

            if (check):
                minus_value += nums[i]
            else:
                plus_value += nums[i]

        return plus_value - minus_value

solution = Solution1541()
solution.calc = input()
print(solution.check_minus())

