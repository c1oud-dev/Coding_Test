def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

# A.remove(obj)
#if not A :