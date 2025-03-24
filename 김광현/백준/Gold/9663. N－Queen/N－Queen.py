def n_queens(row):
    global cnt

    if row == N:  # 모든 행에 퀸을 배치한 경우
        cnt += 1
        return

    for col in range(N):  # 현재 행(row)의 가능한 열(col)을 순회
        if not cols[col] and not diag1[row + col] and not diag2[row - col + (N - 1)]:
            # 퀸을 배치할 수 있는 위치인지 확인
            # diag1[row + col], 우측 상단 왼쪽 아래 대각선은 행과 열의 합이 같으면 대각선이다.
            # diag2[row - col + (N - 1)], 우측 아래 좌측 상단 대각선은 뺀 값이 같으면 된다.
            # diag2의 경우에는 리스트에 넣기 위해서 N-1을 더한 값을 인덱스로 사용하자.

            cols[col] = diag1[row + col] = diag2[row - col + (N - 1)] = True  # 현재 위치에 퀸 배치
            n_queens(row + 1)  # 다음 행 탐색
            cols[col] = diag1[row + col] = diag2[row - col + (N - 1)] = False  # 백트래킹


N = int(input())
cnt = 0
cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
n_queens(0)
print(cnt)
