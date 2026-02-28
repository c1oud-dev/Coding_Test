def solution(phone_book):
    
    hash_map = set(phone_book)  # set 자체가 해시 테이블
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in hash_map:  # O(1) 조회
                return False
    
    return True

# 복잡도 O(NlogN) ~ O(N)