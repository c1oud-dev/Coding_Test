def solution(num_list):
    even = sum(i % 2 == 0 for i in num_list)
    odd = len(num_list) - even
    return [even, odd]