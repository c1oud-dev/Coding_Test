def solution(s):
    stack = []
    
    for bracket in s:
        if not stack or bracket == '(':
            stack.append(bracket)
        else:
            stack.pop()

    return True if not stack else False