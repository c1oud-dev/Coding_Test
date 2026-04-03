import sys

# 1. 재귀 깊이 설정 (필수!)
sys.setrecursionlimit(10**6)

# 2. 입력을 빠르게 받기
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
home = []

# 3. DFS 함수 정의
def dfs(x, y):
    graph[x][y] = 0  # 방문 처리
    count = 1
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

# 4. 전체 탐색
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append(dfs(i, j))

# 5. 결과 출력
print(len(home))
for count in sorted(home):
    print(count)