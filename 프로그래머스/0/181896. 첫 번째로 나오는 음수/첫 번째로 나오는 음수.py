def solution(num_list):
    return next((idx for idx, num in enumerate(num_list) if num < 0), -1)

# next(), enumerate()
# 인덱스와 값 둘 다 쓰면 enumerate, 인덱스만 쓰면 len
# Python 커뮤니티에서는 enumerate를 더 pythonic하다고 본다.