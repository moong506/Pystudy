T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    connect = [0] * (N ** 2 + 1)  # 1번부터 N의 제곱까지니까. 0번 인덱스는 사용X

    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:  # 범위 내이고 1큰수면
                    connect[arr[i][j]] = 1
                    break  # 각 수가 다 다르다고 했음 더 탐색할 필요 X(어차피 걔보다 1큰수 하나뿐임)
    max_cnt = cnt = 1  # 시작하는 수가 1임
    min_num = N ** 2

    for k in range(N ** 2, -1, -1):  # 작은 시작 숫자 찾아야해서 뒤에서부터
        if connect[k]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                min_num = k + 1  # 0이 되어서 멈췄기 때문에 그 직전 k가 마지막 1의 인덱스임
            cnt = 1 # 이제 0이니까 다시 길이 값 초기화

    print(f'#{tc} {min_num} {max_cnt}')