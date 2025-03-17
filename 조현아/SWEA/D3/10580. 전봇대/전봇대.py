T=int(input())
for tc in range(1,T+1):
    N=int(input())
    num=0
    line_list=[]
    for _ in range(N):
        a,b=map(int,input().split())
        line_list.append([a,b])
    for i in range(N-1):
        for j in range(i+1,N):
            # 교차해야 교차점이 생기므로 2가지의 경우의 수에 대해 탐색
            if line_list[i][0]>line_list[j][0] and line_list[i][1]<line_list[j][1]:
                num+=1
            elif line_list[i][0]<line_list[j][0] and line_list[i][1]>line_list[j][1]:
                num+=1
            else:
                continue
    print(f'#{tc} {num}')