T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    lines.sort()

    for i in range(N - 1):
        for j in range(i + 1, N):
            if lines[i][1] > lines[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')