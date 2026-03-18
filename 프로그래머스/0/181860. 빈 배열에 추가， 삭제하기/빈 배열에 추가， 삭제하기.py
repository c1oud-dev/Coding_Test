def solution(arr, flag):
    answer = []
    
    for num, flags in zip(arr, flag):
        if flags == True:
            [answer.append(num) for i in range(num*2)]
        else:
            [answer.pop() for i in range(num)]
    
    return answer