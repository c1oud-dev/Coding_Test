from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    visited = [False] * (y + 1)
    d = deque()

    d.append((x, 0))
    visited[x] = True

    while d:
        num, cnt = d.popleft()

        for nx in [num + n, num * 2, num * 3]:
            if nx == y:
                return cnt + 1
            if nx < y and not visited[nx]:
                visited[nx] = True
                d.append((nx, cnt + 1))
    return -1