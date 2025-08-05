def solution(clothes):
    answer = 1
    clo_dict = {}
    for clo, typ in clothes:
        if typ in clo_dict.keys():
            clo_dict[typ] += 1
        else:
            clo_dict[typ] = 1
    for num in clo_dict.values():
        answer *= (num+1)

    return answer - 1