T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    # 일단 방의 번호를 수정하자. 홀수의 135->123으로, 246->123으로
    for i in range(N):
        if arr[i][0]%2==0: # 첫번째 숫자 수정
            arr[i][0]=arr[i][0]//2
        else:
            arr[i][0]=(arr[i][0]//2)+1
        if arr[i][1]%2==0: # 두번째 숫자 수정
            arr[i][1]=arr[i][1]//2
        else:
            arr[i][1]=(arr[i][1]//2)+1
        if arr[i][0]>arr[i][1]: # 무조건 앞 숫자가 작고 뒷 숫자가 크도록 변경
            arr[i][0],arr[i][1]=arr[i][1],arr[i][0]

    # 주어진 케이스에서 가장 큰 수와 작은 수를 구하자.
    max_num=0
    min_num=200
    range_list=[[] for _ in range(min_num,max_num+1)]
    for i in range(N):
        if arr[i][0]<min_num:
            min_num=arr[i][0]
        if arr[i][1]>max_num:
            max_num=arr[i][1]

    # 각 복도 구간별로 사용 횟수를 저장할 배열 생성
    corridor = [0] * (max_num+ 1) # 인덱스랑 방번호간 차이 조정

    # 각 학생이 지나가는 복도 구간에 +1
    for i in range(N):
        for j in range(arr[i][0], arr[i][1] + 1):
            corridor[j] += 1

    # 가장 많이 겹치는 구간의 횟수가 정답
    max_overlap = max(corridor)

    print(f"#{tc} {max_overlap}")
