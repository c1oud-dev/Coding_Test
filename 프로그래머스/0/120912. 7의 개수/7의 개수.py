def solution(array):
    cnt = 0
    for num in array:
        cnt += str(num).count('7')
    return cnt