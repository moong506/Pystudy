def cal(i,s): # i: 숫자들의 인덱스, s: 한 순열의 합
    global min_v,max_v

    if i == N-1: # 숫자의 마지막 인덱스는 N-1
        min_v = min(min_v, s)
        max_v = max(max_v, s)
        return
    for j in range(4):
        if oper_num[j] > 0:
            oper_num[j] -= 1
            if j == 0:
                cal(i+1,s + nums[i+1])
            elif j == 1:
                cal(i+1,s - nums[i+1])
            elif j == 2:
                cal(i+1,s * nums[i+1])
            elif j == 3:
                if s<0:
                    cal(i+1,-((-s)//nums[i+1]))
                else:
                    cal(i+1,s//nums[i+1])
            oper_num[j] += 1 # 원복시켜야


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    oper_num = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_v = 100000000
    max_v = -100000000

    cal(0,nums[0]) # 한 순열의 합은 첫 숫자에서 시작

    print(f'#{tc} {max_v-min_v}')