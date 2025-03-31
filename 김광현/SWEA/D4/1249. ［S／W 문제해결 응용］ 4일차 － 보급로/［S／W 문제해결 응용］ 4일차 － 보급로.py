import heapq


def dijkstra():  # 2차원 다엑스트라 활용
    pq = [(0, 0, 0)]
    dis = [[float('inf')] * N for _ in range(N)]
    dis[0][0] = 0

    while pq:
        dist, x, y = heapq.heappop(pq)

        if dis[x][y] < dist:
            continue

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = dist + arr[nx][ny]
                if new_dist < dis[nx][ny]:
                    dis[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    return dis[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')