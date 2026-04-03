import sys
sys.setrecursionlimit(10**6) # 1. 재귀 깊이 설정
input = sys.stdin.readline # 2. 입력을 빠르게 받기

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
element = 0 # 연결 요소의 개수

for _ in range(M):
  a, b = map(int, input().split())
  # 인접리스트 생성
  graph[a].append(b)
  graph[b].append(a)


def dfs(idx):
  visited[idx] = True
  
  for i in graph[idx]:
    if not visited[i]:
      dfs(i)
  
for idx in range(1, N + 1):
  if not visited[idx]:
    element += 1
    dfs(idx)
    
print(element)