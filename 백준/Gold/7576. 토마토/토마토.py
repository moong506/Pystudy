M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def find_tomato_day(n, m):
    visited = [[0] * m for _ in range(n)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = [[-1, -1]]*(n*m)
    front = -1
    rear = -1
    result = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                visited[i][j] = 1
                rear += 1
                q[rear] = [i, j]

    while front != rear % (n*m):
        front += 1
        ti, tj = q[front]
        for di, dj in direction:
            ni = ti + di
            nj = tj + dj
            if 0 <= ni <N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[ti][tj] + 1
                    arr[ni][nj] = 1
                    result = visited[ni][nj]
                    rear += 1
                    q[rear] = [ni, nj]
    for i in range(n):  # 익지 않은 토마토인 경우
        for j in range(m):
            if arr[i][j] == 0:
                return -1
    return result -1

ans = find_tomato_day(N,M)

print(ans)