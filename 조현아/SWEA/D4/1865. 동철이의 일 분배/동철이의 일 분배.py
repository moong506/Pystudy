def work(num,cost,N):
    global max_percent
    # 가지치기
    if cost<=max_percent:
        return
    if num == N: # N명의 직원에게 모두 일을 배정해준 경우
        max_percent=max(cost,max_percent)
    else: # 아직 배정해줘야 할 직원이 남은 경우
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                work(num + 1, cost*arr[num][i], N)
                used[i] = 0

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    max_percent=0 # 최댓값 설정
    used=[0]*(N+1)
    work(0,1,N)


    print(f'#{tc} {max_percent*100:.6f}')