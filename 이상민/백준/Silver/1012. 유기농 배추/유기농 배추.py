import sys
input = sys.stdin.readline

queue_i = [0] * 2500
queue_j = [0] * 2500

t = int(input())
for tc in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    visited = [[0] * m for _ in range(n)]
    front = rear = -1
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                result += 1
                rear += 1
                queue_i[rear], queue_j[rear] = i, j
                visited[i][j] = 1
                while front != rear:
                    front += 1
                    ki, kj = queue_i[front], queue_j[front]
                    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                        ni = ki + di
                        nj = kj + dj
                        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                            rear += 1
                            queue_i[rear], queue_j[rear] = ni, nj
                            visited[ni][nj] = 1
    print(result)
