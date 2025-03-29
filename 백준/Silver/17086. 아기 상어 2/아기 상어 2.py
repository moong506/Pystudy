# NxM 배열
from collections import deque

# 8방향 전부
mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]

def bfs():
    while shark:
        x, y = shark.popleft()
        for k in range(8):
            dx = x + mx[k]
            dy = y + my[k]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0:
                    shark.append((dx,dy))
                    arr[dx][dy] = arr[x][y] + 1
    return

n, m = map(int, input().split()) # n행 m열
arr = []

shark = deque()
for i in range(n):
    mat = list(map(int, input().split()))  # n행
    for k in range(m):
        if mat[k] == 1: # 1이면 상어 위치
            shark.append((i,k))
    arr.append(mat)

# 안전거리
bfs()
safe= 0
for i in range(n):
    for j in range(m):
        safe = max(safe, arr[i][j])

print(safe - 1)