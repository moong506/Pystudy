# Baekjoon 2468 안전 영역 (2025.03.10)

# 최대 높이와 최소 구하는 함수
def find_max():
    max_v = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_v:
                max_v = arr[i][j]
    return max_v

# 같은 안전 구역 확인하기
def bfs(h, visited, i, j):
    q = [0] * (N * N)
    front = rear = -1
    # 인큐
    rear += 1
    q[rear] = [i, j]
    visited[i][j] = 1
    while front != rear:
        # 디큐
        front += 1
        i, j = q[front]
        # 상하좌우 순서로 델타 함수 적용
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            """
            인덱스 범위를 벗어나지 않고,
            비에 잠기지 않고,
            방문하지 않았을 때
            """
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > h and visited[ni][nj] == 0:
                # 인큐
                rear += 1
                q[rear] = [ni, nj]
                visited[ni][nj] = 1

# 안전 구역 갯수 구하는 함수
def count_safe_zones(h):
    safe_zones = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 비로 잠기지 않을 때, 방문하지 않았을 때
            if arr[i][j] > h and visited[i][j] == 0:
                bfs(h, visited, i, j)
                safe_zones += 1
    return safe_zones

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 최대 높이와 최소 높이 구하기
max_v = find_max()
# 안전 구역의 최고 값
max_safe_zones = 1
for h in range(max_v):
    # 안전 구역 갯수 구하기
    safe_zones = count_safe_zones(h)
    if max_safe_zones < safe_zones:
        max_safe_zones = safe_zones
print(max_safe_zones)