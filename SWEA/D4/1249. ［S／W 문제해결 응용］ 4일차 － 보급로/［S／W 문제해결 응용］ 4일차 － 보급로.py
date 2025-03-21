def dijkstra(arr, N):
    INF = int(21e8)
    dists = [[INF] * N for _ in range(N)]  # 각 정점까지의 최단 거리를 저장할 리스트
    dists[0][0] = 0  # 시작노드 최단거리는 0
    pq = [(0, 0, 0)]  # 초기화(시간, i, j)

    while pq:
        time, i, j = heapq.heappop(pq)

        if dists[i][j] < time:
            continue

        if i == N - 1 and j == N - 1: # 도착점에 도달하면
            return time

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = arr[ni][nj] # 보수 공사하는데 걸리는 시간
                new_time = time + diff

                if new_time < dists[ni][nj]:
                    dists[ni][nj] = new_time
                    heapq.heappush(pq, (new_time, ni, nj))
    return dists[N - 1][N - 1]



import heapq
INF=int(21e8)  # 21억 (무한대를 의미한다라고 가정)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr_str=[list(input()) for _ in range(N)] # 문자열로 입력받고
    arr = [[int(num) for num in row] for row in arr_str] # 정수로 변환한다.

    result_dists = dijkstra(arr, N)
    print(f'#{tc} {result_dists}')