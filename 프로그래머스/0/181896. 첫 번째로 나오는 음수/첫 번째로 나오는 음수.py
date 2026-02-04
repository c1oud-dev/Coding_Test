def solution(num_list):
    return next((idx for idx, num in enumerate(num_list) if num < 0), -1)