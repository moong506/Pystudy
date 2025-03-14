T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    cnt_list=[0]*(N*N+1)

    for i in range(N):
        for j in range(N):
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ti=i+di
                tj=j+dj
                if 0<=ti<N and 0<=tj<N:
                    if arr[i][j]+1==arr[ti][tj]:
                        cnt_list[arr[i][j]]=1 # 1 입력
                        break # 방향 순회 종료


    # 뒤에서부터 순회를 해야 앞의 위치를 저장할 수 있다.
    start=0
    max_count=0
    count=0
    for m in range(len(cnt_list)-1,-1,-1):
        if cnt_list[m]==1:
            count+=1
            if count >= max_count:
                max_count = count
                start = m
        else:
            count=0

    print(f'#{tc} {start} {max_count+1}')