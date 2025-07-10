def solution(n, w, num):
    answer = 0
    my_floor = num // w
    last_floor = n // w
    
    
    answer += last_floor - my_floor
    
    if n % w == 0:  # 완벽한 직사각형일 경우
        if num % w == 0:
            return answer + 1
        else:
            return answer
    
    if num % w == 0:
        my_floor -= 1
        answer += 1
    
    # 맨 위층 처리 방법
    # 내 위치 판별하기
    if my_floor % 2 == 0:
        if num % w == 0:
            target = w
        else:
            target = num % w
    else:
        if num % w == 0:
            target = 1
        else:
            target = w + 1 - num % w  
    
    if last_floor % 2 == 0: # 맨 윗층이 짝수 -> 역순
        if 1 <= target <= n % w:
            answer += 1
        
    else: # last_floor % 2 == 1
        if w + 1 - n % w <= target <= w:
            answer += 1
    return answer