N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area = 0 # 단지 수
cnt = 0 # 단지에 속하는 집의 수
home = [] # 집의 수를 담을 곳

def dfs(i, j):
  cnt = 1
  
  for k in range(4):
    nx = i + dx[k]
    ny = j + dy[k]
    
    if 0 <= nx < N and 0 <= ny < N:
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        cnt += dfs(nx, ny)
        
  return cnt

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      area += 1
      graph[i][j] = 0
      home.append(dfs(i, j))
      cnt = 0
      

print(area)
for i in sorted(home):
  print(i)