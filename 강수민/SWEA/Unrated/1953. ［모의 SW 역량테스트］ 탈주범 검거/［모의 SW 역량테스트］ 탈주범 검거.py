from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

tunnel_types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def catch_criminal(R, C):
    dq = deque([(R, C)])
    visited[R][C] = 1

    while dq:
        nowy, nowx = dq.popleft()
        dirs = tunnel_types[tunnel[nowy][nowx]]

        for i in range(4):

            # 터널이 없으면 continue
            if dirs[i] == 0:
                continue

            newy = nowy + dy[i]
            newx = nowx + dx[i]

            # 범위 밖으로 나가면 continue
            if newy<0 or newy>=N or newx<0 or newx>=M:
                continue

            # 이미 왔던 곳이면 continue
            if visited[newy][newx]:
                continue

            # 터널이 막혀있으면 continue
            if tunnel[newy][newx] == 0:
                continue

            # 새로운 위치에서 터널 뚫려있는지 확인하기
            new_dirs = tunnel_types[tunnel[newy][newx]]

            if i%2 == 0 and new_dirs[i+1] == 0:
                continue

            if i%2 == 1 and new_dirs[i-1] == 0:
                continue

            # 시간제한에 걸리면 continue
            if visited[nowy][nowx] + 1 > L:
                continue

            # 1시간씩 추가하면서 지나간 곳 기록록
            visited[newy][newx] = visited[nowy][nowx] + 1
            dq.append((newy, newx))


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    # print(tunnel)

    visited = [[0]*M for _ in range(N)]

    catch_criminal(R, C)

    cnt = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')
