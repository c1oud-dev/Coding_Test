def solution(price):
    # 1단계: 조건에 따라 할인율만 결정
    if price < 100000:
        discount = 0
    elif price < 300000:
        discount = 0.05
    elif price < 500000:
        discount = 0.1
    else:
        discount = 0.2
    
    # 2단계: 한 번만 계산
    return int(price * (1 - discount))
