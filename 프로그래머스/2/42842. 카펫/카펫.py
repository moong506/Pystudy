def solution(brown, yellow):
    answer = []
    yellow_list = []
    # 가능한 yellow 조합 찾기
    for h in range(1, yellow+1):
        if yellow % h == 0:
            yellow_list.append([yellow//h,h])
        if yellow//2 <= h:
            break
    # 공식 활용해서 가로, 세로 길이 찾기
    for y_w, y_h in yellow_list:
        if (y_w + y_h + 2) * 2 == brown:
            answer.extend([y_w+2, y_h+2])
            break
            
    
    return answer