def solution(prices):
    
    N = len(prices)
    answer = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
        else:
            answer[i] = j - i
    return answer