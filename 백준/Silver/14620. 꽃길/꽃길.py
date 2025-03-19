def flower(cnt, cost):
    global min_cost
    if cnt == 3:  # 꽃 3개를 심었으면 최소 비용 갱신
        min_cost = min(min_cost, cost)
        return

    if min_cost <= cost:
        return

    for i in range(1, N - 1):  # 가장자리를 제외한 범위에서 탐색
        for j in range(1, N - 1):
            # 꽃을 심을 수 있는지 확인
            if (
                visited[i][j] == 0 and
                visited[i - 1][j] == 0 and
                visited[i + 1][j] == 0 and
                visited[i][j - 1] == 0 and
                visited[i][j + 1] == 0
            ):

                # 비용 계산
                total_cost = (
                    arr[i][j] +
                    arr[i - 1][j] +
                    arr[i + 1][j] +
                    arr[i][j - 1] +
                    arr[i][j + 1]
                )

                # 방문 처리
                visited[i][j] = 1
                visited[i - 1][j] = 1
                visited[i + 1][j] = 1
                visited[i][j - 1] = 1
                visited[i][j + 1] = 1

                # 재귀 호출
                flower(cnt + 1, cost + total_cost)

                # 백트래킹 (되돌리기)
                visited[i][j] = 0
                visited[i - 1][j] = 0
                visited[i + 1][j] = 0
                visited[i][j - 1] = 0
                visited[i][j + 1] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_cost = float('inf')
flower(0, 0)
print(min_cost)
