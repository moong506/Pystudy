from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# DFS이다.
def shoot(cnt, remains, now_arr):
    global min_blocks
    # cnt=구슬을 쏜 횟수
    if cnt == N or remains == 0:  # 구슬을 모두 발사 or 남은 벽돌이 0이면
        # 최소값 갱신 후 종료
        min_blocks = min(min_blocks, remains)
        return # 함수 종료

    # 한 줄 씩 떨구자
    for col in range(W):    # 각 열에 대해
        # 깊은 복사
        copy_arr = [row[:] for row in now_arr]

        # 구슬을 쏘는 열에서 가장 위를 찾기
        row = -1
        for r in range(H):
            if copy_arr[r][col]:  # 벽돌이 있으면 (값이 0이 아니면)
                row = r
                break # for문에서 break

        if row == -1:  # 벽돌이 없는 열이면 다음 열로 (for col로)
            continue

        # BFS
        q = deque([(row, col, copy_arr[row][col])])  # 행, 열, 숫자를 큐에 저장
        now_remains = remains - 1  # 첫 번째 벽돌은 확정적으로 깨짐
        copy_arr[row][col] = 0   # 첫 번째 벽돌 제거

        # 주변 벽돌들이 깨짐
        while q:
            r, c, p = q.popleft()
            for k in range(1, p):   # 벽돌 숫자만큼 영향 범위 확장
                for i in range(4):  # 상하좌우 방향
                    ny = r + (di[i] * k)
                    nx = c + (dj[i] * k)

                    if ny < 0 or ny >= H or nx < 0 or nx >= W:  # 범위 계산
                        continue

                    if copy_arr[ny][nx] == 0:  # 이미 깨진 벽돌이면
                        continue

                    q.append((ny, nx, copy_arr[ny][nx]))  # 다음 벽돌 추가
                    copy_arr[ny][nx] = 0  # 벽돌 깨짐
                    now_remains -= 1  # 숫자 감소


        # 벽돌깨고 아래로 내리기
        # 빈칸을 메꿔주어야 한다
        for c in range(W):  # 각 열에 대해
            idx = H - 1  # 벽돌이 위치할 index   # 맨 아래부터 시작
            for r in range(H - 1, -1, -1):  # 아래에서 위로 순회
                if copy_arr[r][c]:  # 벽돌이 있으면
                    # swap: 현재 벽돌을 아래쪽으로 이동
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1  # 다음 벽돌이 놓일 위치

        shoot(cnt + 1, now_remains, copy_arr)  # 다음 구슬 발사


T = int(input())

for tc in range(1, T + 1):
    # N번 구슬을 쏜다, W=width, H=height
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9  # 최소 남은 벽돌 수 (큰 수로 초기화)
    blocks = 0  # 초기 벽돌 수

    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el:  # 벽돌이 있으면
                blocks += 1

    shoot(0, blocks, arr)  # DFS 시작

    print(f'#{tc} {min_blocks}')