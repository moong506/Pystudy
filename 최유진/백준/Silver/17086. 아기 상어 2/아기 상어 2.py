from collections import deque

def bfs(arr, N, M):
    # 8방향 (상, 하, 좌, 우, 대각선)
    dir = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    # 방문 여부를 나타내는 배열을 0으로 초기화 (0: 미방문, 1: 방문)
    visited = [[0] * M for _ in range(N)]
    # 각 칸까지의 거리를 저장할 배열 (초기값 0)
    ds = [[0] * M for _ in range(N)]
    q = deque()

    # 상어(값이 1인 칸)를 시작점으로 큐에 추가, 방문 처리 및 거리 0으로 설정
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
                ds[i][j] = 0

    # BFS 수행
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                ds[ni][nj] = ds[i][j] + 1
                q.append((ni, nj))

    return ds


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# BFS 실행 후 각 칸까지의 거리 배열 반환
ds = bfs(arr, N, M)

# 전체 칸 중 최대 거리를 결과로 출력
result = max(max(row) for row in ds)
print(result)