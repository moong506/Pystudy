# import sys
# sys.stdin = open('input.txt','r')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

size = 2        # 상어 크기
eat = 0
time = 0

path = 0
path_cnt = 0

# 아기상어를 찾아보자
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            vi, vj = i,j
            arr[i][j] = 0

visited = [[-1]*N for _ in range(N)]
que = []
que.append([vi,vj])
visited[vi][vj] = 0
eatornot = []

while que:

    current_time = 10000

    while que:
        vi, vj = que.pop(0)

        # 현재 위치의 거리가 물고기를 먹을 수 있는 거리와 같다면, 해당 거리는 전부 탐색한 것이다. 먹을 후보를 전부 모은 것.
        if visited[vi][vj] == current_time:
            break

        for di, dj in [[-1,0],[0,-1],[1,0],[0,1]]:      # 위쪽, 좌측을 우선 탐색
            ni, nj = vi+di, vj+dj
            if 0<=ni<N and 0<=nj<N:
                # 상어가 지나갈 수 있고 아직 안 간 곳이면
                if arr[ni][nj] in (0,size) and visited[ni][nj] == -1:
                    que.append([ni,nj])
                    visited[ni][nj] = visited[vi][vj]+1
                # 상어가 먹을 수 있는 물고기인 경우
                elif arr[ni][nj] < size and visited[ni][nj] == -1:

                    visited[ni][nj] = visited[vi][vj] + 1

                    # 일단 먹을 후보에 올려두자
                    eatornot.append([ni,nj])
                    # 현재 거리는?
                    current_time = visited[vi][vj] + 1


    # 먹을 후보가 생겼나?
    if eatornot:
        food_i, food_j = eatornot[0]    # 그럼 가장 위, 왼쪽에 있는 먹이의 좌표를 고르자
        for i,j in eatornot:
            if i<food_i:
                food_i, food_j = i,j
            if i==food_i and j<food_j:
                food_i, food_j = i,j

        eatornot = []

        # 이제 먹자

        arr[food_i][food_j] = 0
        # 현재 위치 제외하고 visited 초기화
        for i in range(N):
            for j in range(N):
                if i != food_i or j != food_j:
                    visited[i][j] = -1
        # 큐도 초기화. 현재 위치가 들어가야함.
        que = []
        que.append([food_i, food_j])
        eat += 1    # 물고기 먹었음
        time = visited[food_i][food_j]      # 물고기를 먹은 시간

        # 사이즈만큼 먹었으면 상어 크기 증가
        if eat == size:
            size += 1
            eat = 0

print(time)