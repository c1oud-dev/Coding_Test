from collections import deque

def solution(priorities, location):
    queue = deque()
    
    queue = deque((index, priority) for index, priority in enumerate(priorities))
    
    answer = []
    while queue:
        index, current = queue.popleft()
        
        for nx, priority in queue:
            if current < priority:
                queue.append((index, current))
                break
        
        if (index, current) not in queue:
            answer.append(index)
    
    return answer.index(location) + 1

                
'''
[A, B, C, D]
우선순위 [2, 1, 3, 2]
실행순서 [C, D, A, B]
3 -> 2 -> 2 -> 1

1. A.2 -> [1, 3, D.2, A.2]
2. B.1 -> [3, D.2, A.2, 1]
3. C.3 -> [D.2, A.2, 1] 3 실행
4. D.2 -> 같은 거 있으면 앞에 잇는게 먼저 실행 -> [A.2, 1] 2 실행
5. A.2 -> [1] 실행
6. D.1 실행
'''