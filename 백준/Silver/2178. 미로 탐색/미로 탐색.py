import sys
input = sys.stdin.readline # 입력을 빠르게 받기

from collections import deque

N, M = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  queue = deque([(i, j)])
  graph[i][j] = int(graph[i][j])
  
  while queue:
    x, y = queue.popleft()
    
    if x == N - 1 and y == M - 1:
      return graph[N - 1][M - 1]
    
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      
      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '1':
          graph[nx][ny] = int(graph[x][y]) + 1
          queue.append((nx, ny))

print(bfs(0, 0))