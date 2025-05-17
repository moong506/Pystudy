from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons_length = len(dungeons)
    for arr in permutations(dungeons, dungeons_length):
        count = 0
        init_num = k
        for min_need_amount, used_amount in arr:
            if min_need_amount > init_num:
                continue
            init_num -= used_amount
            count += 1
        if answer < count:
            answer = count
    return answer