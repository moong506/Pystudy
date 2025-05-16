from itertools import permutations
def solution(numbers):
    answer = 0
    nums = list(numbers)
    num_list = []
    # 순열 생성하기
    for i in range(1, len(nums)+1):
        for per in permutations(nums, i):
            if per[0] == 0:
                continue
            a = int(''.join(per))
            if a <= 1:
                continue
            num_list.append(a)
    num_list = list(set(num_list))
    # 소수인지 판별하는 코드
    for a in num_list:
        for i in range(2, a):
            if a%i == 0:
                break
        else:
            answer += 1

    return answer