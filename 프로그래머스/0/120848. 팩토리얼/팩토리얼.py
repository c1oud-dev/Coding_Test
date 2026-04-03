import math

def solution(n):
    
    for i in range(1, 11):
        if math.factorial(i) > n:
            return i - 1
        elif math.factorial(i) == n:
            return i