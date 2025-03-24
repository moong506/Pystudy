def find_start(arr,n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==9:
                arr[i][j]=0 # 아기상어가 있던 곳을 빈칸으로 만든다.
                return i,j


N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
sti,stj=find_start(arr,N) # 아기 상어의 초기 위치



shark_size=2 # 초기 상어의 크기
ans=0  # 총 이동 시간
count=0  # 먹은 물고기 수

while True:
    # 방문 배열과 큐 초기화 - 새로운 물고기를 찾기 위해 BFS 시작할 때마다 초기화 필요
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append([sti, stj])  # 시작점을 큐에 인큐한다.
    visited[sti][stj] = 1  # 시작점을 방문표시한다.

    fish=[] # 먹을 수 있는 물고기의 위치 저장

    while q:
        ti,tj=q.pop(0)

        # 일단 자기 자신보다 같거나 작은 위치를 탐색해 큐에 넣어보자.
        for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:# 상, 좌, 우, 하
            wi,wj=ti+di,tj+dj
            if 0<=wi<N and 0<=wj<N and visited[wi][wj]==0:

                # 지나갈 수 있는 곳
                if arr[wi][wj]<=shark_size:
                    q.append([wi,wj])
                    visited[wi][wj]=visited[ti][tj]+1


    # shark_size보다 작은 크기의 물고기들간의 우선순위를 정해보자.
    min_dist=N*N
    min_i=-1
    min_j=-1
    for i in range(N):
        for j in range(N):
            # 방문 가능하고, 먹을 수 있는 물고기인 경우 
            # 1. 가장 거리가 가까운 순
            if visited[i][j]>0 and 0<arr[i][j]<shark_size:
                if visited[i][j]<min_dist:
                    min_dist=visited[i][j]
                    min_i,min_j=i,j
            
            # 2. 거리가 같다면 더 윗쪽의 물고기
            elif visited[i][j]==min_dist and i<min_i:
                min_i,min_j=i,j

            # 3. 행도 같다면 더 왼쪽의 열
            elif visited[i][j]==min_dist and i==min_i and j<min_j:
                min_i,min_j=i,j


    if min_i==-1: # 만약 최소거리가 갱신되지 않는 경우
        break

    else:
        # 상어 위치 이동
        ans += min_dist - 1  #visited[sti][stj]=1이므로 1 빼주기
        sti, stj = min_i, min_j  # 새로운 위치 부여
        arr[min_i][min_j] = 0  # 빈칸으로

        count += 1 # 먹은 물고기 수 증가
        if count == shark_size:  # 자기 크기만큼 물고기를 먹었다면
            shark_size += 1  # 크기 증가
            count = 0  # 카운트 초기화

print(ans)


