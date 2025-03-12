from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(arr, a, b):
    n = len(arr)
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
total_cnt = 0  # 단지 총 개수
total_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total_cnt += 1
            result = bfs(arr, i, j)
            total_list.append(result)


print(total_cnt)
total_list.sort()  # 오름차순
for i in range(total_cnt):
    print(total_list[i])
