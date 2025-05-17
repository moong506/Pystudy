from itertools import combinations
def solution(n, q, ans):
    answer = 0
    possible_comb = list(combinations([i for i in range(1, n+1)], 5))
    
    for possible_arr in possible_comb:
        for i in range(len(q)):
            count = 0
            for num in possible_arr:
                if num in q[i]:
                    count += 1
            if count != ans[i]:
                break
        else:
            answer += 1
            
                
            
    return answer