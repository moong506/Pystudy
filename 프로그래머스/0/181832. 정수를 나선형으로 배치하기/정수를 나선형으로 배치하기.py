def solution(n):
    flag = 0
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    ti, tj = 0, 0
    for num in range(2, n**2+1):
        if flag == 1 and 0 <= ti - 1 < n and answer[ti-1][tj] == 0:
            answer[ti-1][tj] = num
            flag = 1
            ti -= 1
        elif 0 <= tj + 1 < n and answer[ti][tj+1] == 0: # 오른쪽
            answer[ti][tj+1] = num
            tj += 1
            flag = 0
        elif 0 <= ti + 1 < n and answer[ti+1][tj] == 0: # 아래
            answer[ti+1][tj] = num
            ti += 1
            flag = 0
        elif 0 <= tj - 1 < n and answer[ti][tj-1] == 0: # 왼쪽
            answer[ti][tj-1] = num
            tj -= 1
            flag = 0
        elif 0 <= ti - 1 < n and answer[ti-1][tj] == 0: # 위쪽
            answer[ti-1][tj] = num
            flag = 1
            ti -= 1
                
    return answer