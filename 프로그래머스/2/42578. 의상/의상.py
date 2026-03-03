from collections import defaultdict

def solution(clothes):
    # 1. 의상 종류별로 개수를 센다
    closet = defaultdict(int)
    for name, kind in clothes:
        closet[kind] += 1
    print(closet)
    # 2. 모든 경우의 수를 곱한다 (각 종류별 개수 + 1)
    answer = 1
    for count in closet.values():
        answer *= (count + 1)
    
    # 3. 아무것도 입지 않은 경우 1개를 뺀다
    return answer - 1
    

    
# 의상 종류가 같은 것끼리 묶기
# dict - {'yellow_hat': 'headgear', 'blue_sunglasses': 'eyewear', 'green_turban': 'headgear'}
# 문제는 의상이 1개 이상일 때 묶이지 않음
# for문으로 dict 만들기