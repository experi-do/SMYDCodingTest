def solution(nums):
    N = len(nums)/2
    nums = set(nums)
    print('nums: ', nums)
    if (len(nums) >= N):
        answer = N
    else:
        answer = len(nums)
        
    return answer