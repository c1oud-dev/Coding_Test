def solution(tickets):
    # 1. 사전순으로 앞선 경로를 먼저 찾기 위해 티켓 정렬
    tickets.sort()
    
    # 2. 방문 여부를 체크할 리스트
    visited = [False] * len(tickets)
    
    def dfs(current_airport, path):
        # 3. 종료 조건: 모든 티켓을 사용했을 때 (공항 수는 티켓 수 + 1)
        if len(path) == len(tickets) + 1:
            return path
        
        for idx, (start, end) in enumerate(tickets):
            # 4. 아직 사용하지 않은 티켓 중, 출발지가 현재 공항과 일치하는 경우
            if not visited[idx] and start == current_airport:
                visited[idx] = True
                
                # 5. path + [end]를 통해 새로운 리스트를 전달 (재귀)
                result = dfs(end, path + [end])
                
                # 6. 만약 이 경로로 끝까지 완성이 되었다면 그대로 반환
                if result:
                    return result
                
                # 7. 완성되지 않았다면 다시 티켓을 미사용 상태로 (Backtracking)
                visited[idx] = False
        
        return None

    # 8. 항상 "ICN"에서 시작
    return dfs("ICN", ["ICN"])
            