import sys
from collections import deque
input = sys.stdin.readline

def find_unripe_tomatoes(N, M, H):
    for k in range(H):
        for j in range(M):
            for i in range(N):
                if arr[k][j][i] == 0:
                    return 1
    return 0

def bfs(n, m, h):
    visited = [[[-1] * n for _ in range(m)] for _ in range(h)]
    q = deque()
    for k in range(H):
        for j in range(M):
            for i in range(N):
                if arr[k][j][i] == 1:
                    q.append([i, j, k])
                    visited[k][j][i] = 0

    dh = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]

    while q:
        tx, ty, th = q.popleft()
        for i in range(6):
            nx = tx + dx[i]
            ny = ty + dy[i]
            nh = th + dh[i]
            # 인덱스 안벗어남
            if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h:
                # 처음 방문했고, 안 익은 토마토!
                if visited[nh][ny][nx] == -1 and arr[nh][ny][nx] == 0:
                    visited[nh][ny][nx] = visited[th][ty][tx] + 1
                    arr[nh][ny][nx] = 1
                    q.append([nx, ny, nh])

    if find_unripe_tomatoes(n, m, h):
        return -1

    max_num = 0
    for k in range(H):
        for j in range(M):
            if max_num < max(visited[k][j]):
                max_num = max(visited[k][j])

    return max_num


N, M, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

ans = bfs(N, M, H)
print(ans)
