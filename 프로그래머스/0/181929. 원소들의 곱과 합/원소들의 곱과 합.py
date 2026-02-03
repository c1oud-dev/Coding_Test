def solution(num_list):
    answer = 1
    for num in num_list:
        answer *= num
    return int(sum(num_list)**2 > answer)