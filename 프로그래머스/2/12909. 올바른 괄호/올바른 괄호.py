def solution(s):
    answer = True
    top = -1
    for i in s:
        if i == '(':
            top += 1
        else:  # i == ')'
            if top >= 0:
                top -= 1
            else:
                answer = False
                break
    else:
        if top != -1:
            answer = False

    return answer