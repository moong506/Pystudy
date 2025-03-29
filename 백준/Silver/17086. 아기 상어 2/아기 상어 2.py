# 아기상어 2
def find_length(x,y,arr,n,m):
    dq = deque([(x, y, 0)])  # (행, 열, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True # 시작점 방문 표시

    while dq:
        i, j, dist = dq.popleft()

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
            mi,mj=i+di,j+dj
            if 0<=mi<n and 0<=mj<m and visited[mi][mj]==False:
                if arr[mi][mj]==1:
                    return dist+1
                visited[mi][mj]=True
                dq.append((mi,mj,dist+1))

    return 0 # 찾지 못한 경우


def bfs(N,M):
    max_length=0 # 작은 수로 초기화
    for i in range(N):
        for j in range(M):
            length=0 # 모든 좌표에서 초기화
            if arr[i][j]==0: # 빈 칸에서의 안전거리를 구하기.
                length=find_length(i,j,arr,N,M)
                max_length=max(max_length,length)
    return max_length


from collections import deque
N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
result=bfs(N,M)
print(result)