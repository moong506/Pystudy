import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우 좌상 좌하 우상 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
result = 0

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 0인 경우만 거리 측정(이전 위치에서의 거리 + 1)
            if not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

for x in range(N):
    for y in range(M):
        if arr[x][y]:
            # 상어 위치 q에 추가
            q.append((x, y))

bfs()
for a in arr:
    result = max(max(a), result)

print(result - 1)
# 1부터 시작하므로 최종 결과인 거리는 1을 빼줘야 한다
