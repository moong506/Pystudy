def f(i, N, p):         # i 사람 번호 N 사람 수 p i-1사람까지의 성공 확률
    global max_v
    if i == N:          # 모든사람의 일이 결정된 경우
        if max_v < p:
            max_v = p
    elif max_v >= p:    # 백트래킹
        return
    else:
        for j in range(N):
            if used[j] == 0:    # j번 일을 맡은 사람이 없으면
                used[j] = 1
                f(i+1, N, p*(Pij[i][j]/100))    # Pij가 %이므로 100으로 나눠줌
                used[j] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Pij = [list(map(int, input().split())) for _ in range(N)]

    work = [0] * N      # work[i] i번 사람이 맡은 일의 번호
    used = [0] * N      # 남겨진 일 확인용
    max_v = 0
    f(0, N, 1)

    print(f'#{tc} {max_v*100:.6f}')