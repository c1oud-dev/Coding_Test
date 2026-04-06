def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []
    for idx, alpha in enumerate(str_list):
        if alpha == 'l':
            return str_list[:idx]
        elif alpha == 'r':
            return str_list[idx + 1:]