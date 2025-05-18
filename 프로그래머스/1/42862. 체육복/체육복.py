def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    find = lost[:]
    # 도난 당한 사람 미리 처리
    for l in lost:
        if l in reserve:
            reserve.pop(reserve.index(l))
            find.pop(find.index(l))
        
    
    lost = find[:]
    for l in lost:
        if l-1 in reserve:
            
            find.pop(find.index(l))
            reserve.pop(reserve.index(l-1))
        elif l+1 in reserve:
            find.pop(find.index(l))
            reserve.pop(reserve.index(l+1))
    
    
    answer = n - len(find)
    
    
    return answer