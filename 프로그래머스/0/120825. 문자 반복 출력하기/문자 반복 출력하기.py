def solution(my_string, n):
    return "".join([i*n for i in list(map(str, my_string))])
