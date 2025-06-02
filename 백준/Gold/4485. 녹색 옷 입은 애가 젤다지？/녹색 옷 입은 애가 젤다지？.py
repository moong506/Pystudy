from collections import deque
tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = arr[0][0]
    q = deque([[0,0]])
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti+di, tj+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if visited[ni][nj] == -1:
                visited[ni][nj] = visited[ti][tj] + arr[ni][nj]
                q.append([ni, nj])
            elif visited[ni][nj] > visited[ti][tj] + arr[ni][nj]:
                visited[ni][nj] = visited[ti][tj] + arr[ni][nj]
                q.append([ni, nj])
    print(f'Problem {tc}: {visited[N-1][N-1]}')
    tc += 1

