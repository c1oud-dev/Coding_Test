from collections import deque

def solution(begin, target, words):
    # 1. 예외 처리: target이 없으면 바로 종료
    if target not in words:
        return 0

    # 2. set을 활용해 남은 단어들(미방문)을 관리 (성능 UP)
    word_set = set(words)
    queue = deque([(begin, 0)])
    # 시작 단어는 words에 없을 수도 있으므로 따로 관리할 필요 없음

    while queue:
        current, cnt = queue.popleft()

        if current == target:
            return cnt

        # 3. '방문 가능한' 단어들만 추출하기 위한 리스트
        converted_words = []
        
        for word in word_set:
            # 한 글자만 다른지 확인
            if sum(1 for a, b in zip(current, word) if a != b) == 1:
                queue.append((word, cnt + 1))
                converted_words.append(word)
        
        # 4. 큐에 넣은 단어는 '미방문 단어 집합'에서 제거 (visited.add 역할)
        for word in converted_words:
            word_set.remove(word)

    return 0