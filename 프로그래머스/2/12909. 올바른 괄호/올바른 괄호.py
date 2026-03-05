def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
            
    return not stack