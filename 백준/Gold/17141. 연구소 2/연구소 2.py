from itertools import combinations
from collections import deque

# 0. 바이러스를 놓을 수 있는 칸 찾기 함수
def find_virus(n):
    lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                lst.append([i, j])
    return lst

# 1. 바이러스를 퍼트려서 걸리는 시간 찾는 함수
def find_min_time(init_virus, n):
    q = deque(list(init_virus))
    visited = [[-1] * n for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 미리 방문 체크
    for x, y in q:
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n:
                if visited[tx][ty] == -1:
                    if arr[tx][ty] == 1:
                        continue
                    visited[tx][ty] = visited[x][y] + 1
                    q.append([tx, ty])
    max_num = -1

    for i in range(N):
        for j in range(N):
            if visited[i][j] > max_num:
                max_num = visited[i][j]
            if arr[i][j] != 1 and visited[i][j] == -1:
                return -1

    return max_num

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = find_virus(N)
min_t = 2500
for lst in combinations(virus, M):
    result = find_min_time(lst, N)
    if result != -1:
        if min_t > result:
            min_t = result
if min_t == 2500:
    print(-1)
else:
    print(min_t)