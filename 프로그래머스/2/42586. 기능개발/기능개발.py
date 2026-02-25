import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - progress) / speed)  for progress, speed in zip(progresses, speeds)]
    stack = []
    
    for day in days:
        if not stack or day <= stack[0]:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack = [day]
    print(stack)
    answer.append(len(stack))
    return answer