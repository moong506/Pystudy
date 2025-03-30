from collections import deque

# 시작점 찾기
def find_start():
    result = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                result.append((i, j))
    return result

# bfs
def bfs(start):
    dq = deque()
    visited = [[-1] * M for _ in range(N)]
    # 시작점 인큐
    for i, j in start:
        dq.append((i, j))
        visited[i][j] = 0
    while dq:
        # 디큐
        i, j = dq.popleft()
        # 상하좌우, 왼위대, 오위대, 오아대, 왼아대
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1 and visited[ni][nj] == -1:
                # 인큐
                dq.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # 최대 안전 거리 찾기
    max_distance = 0
    for i in range(N):
        for j in range(M):
            if max_distance < visited[i][j]:
                max_distance = visited[i][j]
    return max_distance

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(find_start()))