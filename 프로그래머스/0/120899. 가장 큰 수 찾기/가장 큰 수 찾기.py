def solution(array):

    idx, value = max(enumerate(array), key=lambda x: x[1])
    return [value, idx]