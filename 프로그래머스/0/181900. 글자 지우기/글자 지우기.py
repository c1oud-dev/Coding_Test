def solution(my_string, indices):
    my_str_list = list(my_string)
    for i in indices:
        my_str_list[i] = ''
    return ''.join(my_str_list)