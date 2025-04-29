def find_start_idx():
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if arr[l][r][c] == 'S':
                    return l, r, c

def bfs(stL, stR, stC):
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    visited[stL][stR][stC] = 1
    q = [[0, 0, 0]] * (L*R*C)
    front = -1
    rear = 0
    q[rear] = [stL, stR, stC]

    while front != rear % (L*R*C):
        front += 1
        tl, tr, tc = q[front]
        for dl, dr, dc in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            nl, nr, nc = tl+dl, tr+dr, tc+dc
            if 0<=nl<L and 0<=nr<R and 0<=nc<C:
                if arr[nl][nr][nc] =='E':  # 도착 지점 찾음
                    return visited[tl][tr][tc]
                if visited[nl][nr][nc] == 0 and arr[nl][nr][nc] =='.': # 갈 수 있는 곳 찾음
                    rear += 1
                    q[rear] = [nl, nr, nc]
                    visited[nl][nr][nc] = visited[tl][tr][tc] + 1

    return -1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr = [0]*L
    for l in range(L):
        arr[l] = [list(input()) for _ in range(R)]
        blank = input()

    startL, startR, startC = find_start_idx()
    ans = bfs(startL, startR, startC)
    if ans != -1:  # 탈출 못한 경우
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')
