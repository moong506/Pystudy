from collections import deque
 
tunnel_type = { # 터널 유형별로 어디로 이어지는 지
        1: [(0, 1), (1, 0), (0, -1), (-1, 0)],  # 우하좌상
        2: [(1, 0), (-1, 0)],
        3: [(0, 1), (0, -1)],
        4: [(0, 1), (-1, 0)],
        5: [(0, 1), (1, 0)],
        6: [(1, 0), (0, -1)],
        7: [(0, -1), (-1, 0)]
    }
 
T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # 세로 가로 맨홀세로 멘홀가로 시간
    tunnel = [list(map(int, input().split())) for _ in range(N)]
 
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    que = deque()
    que.append((R, C))
    
    cnt = 1 # 1시간에 맨홀 부분이라 했으니까
    while que:
        pi, pj = que.popleft()
 
        for di, dj in tunnel_type[tunnel[pi][pj]]:
            ni = pi + di
            nj = pj + dj
 
            if 0 <= ni < N and 0 <= nj < M and tunnel[ni][nj] != 0 and visited[ni][nj] == 0: # 범위 안이고 터널이고 방문한 적 없으면
                if visited[pi][pj] < L and (-di, -dj) in tunnel_type[tunnel[ni][nj]]: # 시간 범위 안이고, 방문하려는 곳이 지금 장소와 연결되어 있을 때 (지금 (1,0)으로 가려고 하면 방문 위치는 (-1,0)이 뚫려있어야 함)
                    que.append((ni, nj))
                    visited[ni][nj] = visited[pi][pj] + 1
                    cnt += 1
 
    print(f'#{tc} {cnt}')