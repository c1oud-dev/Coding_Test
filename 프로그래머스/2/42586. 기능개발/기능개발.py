import math

def solution(progresses, speeds):
    days = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    
    stack = []
    answer = []
    for day in days:
        if not stack or stack[0] >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack = []
            stack.append(day)
            
    answer.append(len(stack))
    return answer 

