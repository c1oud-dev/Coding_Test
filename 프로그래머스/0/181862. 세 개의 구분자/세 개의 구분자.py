def solution(myStr):
    str_list = myStr.replace('a', " ").replace('b', " ").replace('c', " ").split(' ')
    result = []
    
    for i in str_list:
        if i != "":
            result.append(i)
    
    return result if len(result) != 0 else ["EMPTY"]