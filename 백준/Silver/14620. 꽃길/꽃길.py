# (자기자신, 상, 우, 하, 좌)
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]


def check(i, j):
    """
    현재 위치에 꽃을 심을 수 있는지 확인하는 함수
    꽃은 중앙과 상하좌우에 씨앗이 필요하므로 5칸을 확인
    """
    for x in range(5):
        nx = i + dx[x]
        ny = j + dy[x]

        # 이미 방문한 곳이라면 심을 수 없음
        if visited[nx][ny] == True:
            return False

    # 모든 칸이 비어있다면 꽃을 심을 수 있음
    return True


def dfs():
    global cnt, ans, cost

    # 꽃 3개를 모두 심었을 떄
    if cnt == 3:
        # 최소 비용 갱신
        ans = min(ans, cost)
        return

    # 꽃의 중앙 위치를 결정하기 위해 모든 칸을 순회
    # 가장자리는 꽃잎이 밖으로 나가므로 1부터 N-2까지만 확인
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 현재 위치에 꽃을 심을 수 있는지 확인
            if check(i, j):
                # 꽃 개수 증가
                cnt += 1
                # 꽃을 심고 방문 표시 및 비용 계산
                for k in range(5):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    visited[ni][nj] = True  # 방문 표시
                    cost += flower[ni][nj]  # 비용 추가


                dfs()  # 다음 꽃을 심기 위한 재귀 호출

                # 백트래킹: 현재 꽃을 제거하고 다른 위치에 심어보기
                cnt -= 1
                for k in range(5):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    visited[ni][nj] = False  # 방문 표시 제거
                    cost -= flower[ni][nj]  # 비용 제거


N = int(input())
flower = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

cnt = 0  # 현재까지 심은 꽃의 개수
cost = 0  # 현재까지의 총 비용
ans = float('inf')  # 최소 비용

dfs()

print(ans)