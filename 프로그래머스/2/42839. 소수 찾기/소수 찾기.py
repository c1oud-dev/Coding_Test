from itertools import permutations

def solution(numbers):
    # 1. 모든 가능한 숫자 조합 만들기
    candidates = set()
    
    for cnt in range(1, len(numbers) + 1):
        for perm in permutations(numbers, cnt):
            num_str = ''.join(perm)
            if num_str[0] != '0':  # 0으로 시작하는 숫자 제외
                candidates.add(int(num_str))
    
    # 2. 소수 개수 세기
    answer = 0
    for num in candidates:
        if is_prime(num):
            answer += 1
    
    return answer

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True