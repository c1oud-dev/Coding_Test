import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:   # 섞어도 K이상이 안 될 때
            return -1
        
        first = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, first + sec * 2)
        cnt += 1
    
    return cnt