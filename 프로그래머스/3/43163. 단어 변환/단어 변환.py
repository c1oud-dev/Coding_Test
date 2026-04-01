from collections import deque

def solution(begin, target, words):
    # words 개수만큼 방문 리스트 만들기
    visited = set()
    
    # words target이 없으면 바로 0 반환
    if target not in words: return 0
    
    # 시작 상태를 큐에 삽입 (단어, 변환 횟수 0)
    queue = deque([(begin, 0)])
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == target:
            return cnt
        
        for word in words:
            # 두 단어의 각 자리를 비교해서 서로 다른 것들의 합이 1인지 확인
            if sum(1 for a, b in zip(current, word) if a != b) == 1:
                # 2. 여기서 '아직 방문하지 않은 단어'인지 확인
                if word not in visited:
                    # 3. 큐에 넣을 때 cnt + 1로 넘겨주기
                    queue.append((word, cnt + 1))
                    # 4. 넣은 단어는 다시 방문하지 않게 기록하기
                    visited.add(word)

