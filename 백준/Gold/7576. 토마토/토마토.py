from collections import deque

def find_ans():
    global ans
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] != -1:
                return -1
            else:
                if ans < visited[i][j]:
                    ans = visited[i][j]
    return ans-1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque([])
ans = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 1
while q:
    ti, tj = q.popleft()
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = ti + di, tj + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = visited[ti][tj] + 1
            q.append((ni,nj))
print(find_ans())
