import sys
input = sys.stdin.readline
from collections import deque

# 먹을 수 있는 물고기가 있는지 판별하는 함수
def check_available_fish(n, vis, sz):
    min_dist = 1e7
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] < sz and 0 < vis[i][j] < min_dist:
                min_dist= vis[i][j]
                x, y = i, j
    return [min_dist, x, y]

# 먹을 수 있는 물고기의 위치 별로 거리를 계산하는 함수
def calculate_distance(n, start_i, start_j ,sz):
    # 이 아래에서 bfs로 길 찾기 수행
    visited = [[0] * n for _ in range(n)]
    visited[start_i][start_j] = 1
    q = deque()
    q.append([start_i, start_j])
    while q:
        ti, tj = q.popleft()
        for i in range(4):
            ni = ti + di[i]
            nj = tj + dj[i]
            # 인덱스 벗어나면 종료
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            # 이미 방문한 곳도 종료
            if visited[ni][nj] > 0:
                continue
            # 아기 상어의 크기(sz)보다 크면 갈 수 없으므로 종료
            if arr[ni][nj] > sz:
                continue
            visited[ni][nj] = visited[ti][tj] + 1
            q.append([ni, nj])
    return visited

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
dist = 0
eaten = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
sti, stj = 0, 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sti = i
            stj = j
            break

while True:
    # 1. 상어 위치 기준으로 bfs 돌리기
    visit = calculate_distance(N, sti, stj ,size)
    fish_dist, fish_i, fish_j = check_available_fish(N, visit, size)

    # 갈 수 없어서 먹이를 먹지 못하는 경우
    if fish_dist == 1e7:
        print(dist)
        break
    # 2. 물고기 이동 후 먹기
    dist += fish_dist - 1
    eaten += 1

    # 위치 초기화
    arr[sti][stj] = 0
    arr[fish_i][fish_j] = 0
    sti, stj = fish_i, fish_j
    
    # 사이즈 초기화
    if size == eaten:
        size += 1
        eaten = 0


