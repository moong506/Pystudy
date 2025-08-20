from collections import deque
def bfs(n, m):
    visited = [[0]* m for _ in range(n)]
    q = deque()
    max_num = 0
    # 초깃값 구하기
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                visited[i][j] = 1
                q.append([i, j])
    
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            ni, nj = ti + di, tj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if visited[ni][nj] != 0:
                continue
            visited[ni][nj] = visited[ti][tj] + 1
            if max_num < visited[ni][nj]:
                max_num = visited[ni][nj]
            q.append([ni, nj])
    return max_num - 1
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = bfs(N, M)
print(ans)
