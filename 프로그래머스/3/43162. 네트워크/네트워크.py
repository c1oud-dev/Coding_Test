def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            count += 1
            
    return count
    
def dfs(n, computers, i, visited):
    visited[i] = True
    
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(n, computers, j, visited)