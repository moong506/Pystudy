
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    day = [0]*N  # stack
    top = 0
    day[0] = (100-progresses[0])//speeds[0] + 1  # 초깃값 설정
    if (100-progresses[0]) % speeds[0] == 0:
            day[0] -= 1
    
    for i in range(1, N):
        quest = (100-progresses[i])//speeds[i] + 1
        if (100-progresses[i]) % speeds[i] == 0:
            quest -= 1
        if day[0] >= quest:
            top += 1
            day[top] = quest
        else:
            answer.append(top+1)
            top = 0
            day[0] = quest
    answer.append(top+1)
    
    
        
    return answer