def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0
    #return int(my_string.endswith(is_suffix))
