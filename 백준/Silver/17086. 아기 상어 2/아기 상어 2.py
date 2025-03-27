N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
while q:
    ti, tj = q.pop(0)
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]:
        ni, nj = ti + di, tj + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = visited[ti][tj] + 1
            q.append((ni,nj))
# print(visited)
max_visit = 0
for i in range(N):
    for j in range(M):
        if max_visit < visited[i][j]:
            max_visit = visited[i][j]
print(max_visit)