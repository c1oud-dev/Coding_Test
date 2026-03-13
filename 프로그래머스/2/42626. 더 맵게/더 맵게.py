import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K and len(scoville) >= 2:
        first = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, first + sec * 2)
        cnt += 1
        if scoville[0] >= K:
            return cnt
    
    if scoville[0] >= K:
        return cnt
    
    return -1