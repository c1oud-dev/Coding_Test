def solution(nums):
    answer = 0
    
    s = set(nums)   # 중복 제거
    if len(s) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(s)