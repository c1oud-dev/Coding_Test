def solution(arr, idx):
    for index, num in enumerate(arr[idx:]):
        if num == 1:
            return index + idx
    return -1