def n_queens(row):
    global cnt

    if row == N:  # 모든 행에 퀸을 배치한 경우
        cnt += 1
        return

    for col in range(N):  # 현재 행(row)의 가능한 열(col)을 순회
        # 같은 열에 없고,/대각선에 없고, \대각선에 없는 경우
        if not cols[col] and not diag1[row + col] and not diag2[row - col + (N - 1)]:
            cols[col] = diag1[row + col] = diag2[row - col + (N - 1)] = True  # 현재 위치에 퀸 배치
            n_queens(row + 1)  # 다음 행 탐색
            cols[col] = diag1[row + col] = diag2[row - col + (N - 1)] = False  # 백트래킹


N = int(input())
cnt = 0
cols = [False] * N      # 각 열에 퀸이 있는지 확인
diag1 = [False] * (2 * N - 1) # /우측 상단에서 좌측 하단으로 내려가는 대각선 (행+열 값이 같은 칸들)
diag2 = [False] * (2 * N - 1) # \좌측 상단에서 우측 하단으로 내려가는 대각선 (행-열 값이 같은 칸들)
n_queens(0)
print(cnt)