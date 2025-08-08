def bfs(N,M):
    visited = [[0]* M for _ in range(N)]
    visited[0][0] = 1
    q = [[0,0]]
    while q:
        ti, tj = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '1':
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = visited[ti][tj] + 1
                        if ni == N - 1 and nj == M - 1:
                            return visited[ni][nj]
                        q.append([ni,nj])

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
print(bfs(n,m))

