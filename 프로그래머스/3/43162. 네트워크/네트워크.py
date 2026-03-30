def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
    
    return answer

def dfs(n, computers, v, visited):
    visited[v] = True
    
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(n, computers, i, visited)