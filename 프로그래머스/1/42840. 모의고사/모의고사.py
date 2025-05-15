def solution(answers):
    score_1 = 0
    score_2 = 0
    score_3 = 0
    answer = []
    for i in range(len(answers)):
        # 1번 수포자의 채점 방식 : 5를 나눈 나머지 + 1
        if i % 5 + 1 == answers[i]:
            score_1 += 1
        # 2번 수포자
        if i%2 == 0:
            if answers[i] == 2:
                score_2 += 1
        elif i%8 == 1:
            if answers[i] == 1:
                score_2 += 1
        elif i%8 == 3:
            if answers[i] == 3:
                score_2 += 1
        elif i%8 == 5:
            if answers[i] == 4:
                score_2 += 1
        else:
            if answers[i] == 5:
                score_2 += 1
        
        # 3번 수포자
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                score_3 += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                score_3 += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                score_3 += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                score_3 += 1
        else:
            if answers[i] == 5:
                score_3 += 1

    if score_1 >= score_2 and score_1 >= score_3:
        answer.append(1)
    if score_2 >= score_1 and score_2 >= score_3:
        answer.append(2)
    if score_3 >= score_1 and score_3 >= score_2:
        answer.append(3)
    
    return answer