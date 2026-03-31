def solution(i, j, k):
    count = 0
    for num in range(i, j + 1):
        for v in str(num):
            if v == str(k):
                count += 1
    return count