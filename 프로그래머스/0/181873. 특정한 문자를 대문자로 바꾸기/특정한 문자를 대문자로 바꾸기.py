def solution(my_string, alp):
    return my_string.replace(alp, my_string[my_string.find(alp)].upper())