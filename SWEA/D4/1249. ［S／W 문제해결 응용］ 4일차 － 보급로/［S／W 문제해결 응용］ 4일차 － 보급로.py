import heapq

def dijkstra():
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0

    pq = [(0, 0, 0)] # 누적합, 현재i,현재j

    while pq:
        w, pi, pj = heapq.heappop(pq) # 지금 pq 중에 제일 작은 값

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = pi + di
            nj = pj + dj

            if 0 <= ni < N and 0 <= nj < N:
                new_dist = w + MAP[ni][nj] # 끌고 온 누적합에 이동한 위치의 깊이만큼 더함

                if ni == N - 1 and nj == N - 1: # 이동한 곳이 끝임(도착함)
                    return new_dist

                if dists[ni][nj] > new_dist: # 지금 온 방향에서의 누적합과 원래 저장된 누적합 비교
                    dists[ni][nj] = new_dist

                    heapq.heappush(pq, (new_dist,ni,nj))

    return dists[N-1][N-1]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input())) for _ in range(N)]

    ans = dijkstra()
    print(f'#{tc} {ans}')