
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    room_num = [1] * (N ** 2 + 1)

    for i in range(N):
        for j in range(N):
            ti, tj = i, j 
            while True:
                if room_num[rooms[ti][tj]] > 1: 
                    break
                for di, dj in delta:
                    ni, nj = ti + di, tj + dj
                    if 0 <= ni < N and 0 <= nj < N: 
                        if rooms[ni][nj] - rooms[ti][tj] == 1:
                            room_num[rooms[i][j]] += room_num[rooms[ni][nj]]
                            ti, tj = ni, nj
                            break
                else:
                    break
    max_room = 0
    for r in range(N ** 2 + 1):
        if room_num[max_room] < room_num[r]:
            max_room = r
    print(f'#{tc} {max_room} {room_num[max_room]}')