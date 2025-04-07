from collections import deque


def bfs(sti, stj):
    visited = [[0] * C for _ in range(R)]
    visited[sti][stj] = 1
    q = deque()
    q.append((sti, stj))
    max_v = 1
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < R and 0 <= nj < C:  # 인덱스 범위에 존재
                if arr[ni][nj] == 'L' and visited[ni][nj] == 0:  # 방문 안한 땅
                    visited[ni][nj] = visited[ti][tj] + 1
                    q.append([ni, nj])
                    if max_v < visited[ni][nj]:
                        max_v = visited[ni][nj]
    return max_v - 1


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
max_distance = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            max_distance = max(bfs(i, j), max_distance)

print(max_distance)