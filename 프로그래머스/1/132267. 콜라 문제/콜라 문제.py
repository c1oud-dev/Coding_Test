def solution(a, b, n):
    answer = 0
    while n >= a:
        bottles = (n // a) * b
        answer += bottles
        n = (n % a) + bottles
    return answer