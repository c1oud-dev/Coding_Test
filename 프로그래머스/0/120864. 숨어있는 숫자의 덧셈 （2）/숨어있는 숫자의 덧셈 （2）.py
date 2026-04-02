def solution(my_string):
    for alpha in my_string:
        if not alpha.isdigit():
            my_string = my_string.replace(alpha, ' ')
    
    return sum(map(int, my_string.split()))