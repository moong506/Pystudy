from collections import deque
def f(N, M, R, C, L):
    # 행 N, 열 M, 맨홀 위치 (R,C), 시간 L
    dq = deque([(R, C)])
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1  # 시간
    # pos = [0] *(L+1)  # 시간대별 가능 위치 수
    cnt = 0

    while dq:
        i, j = dq.popleft() # 새로운 현재 위치
        cnt += 1
        # pos[v[i][j]] += 1 # 시간대에 도착하는 칸 번호
        if visited[i][j] < L:  # L초 미만에 도착한 칸이면
            # 만약 조건이 visited[i][j] <= L이었다면, 시간 L에 도달한 칸에서도 다음 칸을 탐색하게 되어 시간 L+1인 칸까지 큐에 추가되게 됩니다
            for x in pipe[arr[i][j]]:  # 파이프 모양에 따라 새롭게 진입할 칸 확인
                ni = i + di[x]
                nj = j + dj[x]
                # 이동할 위치가 격자 범위 내에 있고, 0이 아니며, 방문한적 없고,
                # 현재 뚫여있는 곳이 우 이면 좌, 상 이면 하가 새로 이동할 좌표에 뚫려있는지 확인.
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0 and (x + 2) % 4 in pipe[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1  # 이동할 수 있는 칸에 시간
                    dq.append((ni, nj))
    # return sum(pos)
    return cnt

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 파이프의 숫자를 인덱스로 해, 우하좌상에서 파이프가 뚫려있는 방향 저장.
pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, R, C, L)
    print(f'#{tc} {r}')