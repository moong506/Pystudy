import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        if len(scoville) == 0:
            return -1
        else:
            b = heapq.heappop(scoville)
            if b == 0:
                if K == 0:
                    return 0
                else:
                    return -1
            heapq.heappush(scoville, a+b*2)
            answer += 1
    return answer