import sys
from collections import deque

# 8방향 이동
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

def bfs():
    while queue:
        i, j = queue.popleft()
        
        for idx in range(8):
            ni = i + di[idx]
            nj = j + dj[idx]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)] # 거리 저장 배열
queue = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1: # 상어를 만나면(상어로부터 잴 것임)
            queue.append((i, j))
            visited[i][j] = 0 # 여기서부터 시작할거니까 0으로 재할당

bfs()

max_cnt = max(max(row) for row in visited)
print(max_cnt)
