def solution(arr1, arr2):
    answer = 0
    result = len(arr1)-len(arr2)
    if result > 0:
        answer = 1
    elif result < 0:
        answer = -1
    else:
        if sum(arr1) > sum(arr2):
            answer =1 
        elif sum(arr1) < sum(arr2):
            answer =-1
        else:
            answer
    return answer