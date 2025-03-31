from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [
    (-1, 0),  # 상
    (-1, 1),  # 상우
    (0, 1),   # 우
    (1, 1),   # 하우
    (1, 0),   # 하
    (1, -1),  # 하좌
    (0, -1),  # 좌
    (-1, -1)  # 상좌
]
safe = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            continue
        q = deque()
        visited = [[-1] * M for _ in range(N)]
        q.append([x, y])
        visited[x][y] = 0
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    if arr[ni][nj] == 1:
                        safe = max(safe, visited[ni][nj])
                        q = deque()
                        break
print(safe)