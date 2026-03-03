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