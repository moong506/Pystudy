T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    comb = [[0, 0]]

    dp = [[0]*(L+1) for _ in range(N+1)]

    for _ in range(N):
        comb.append(list(map(int, input().split())))

    for i in range(1, N+1):
        for j in range(1, L+1):
            rates = comb[i][0]
            kcal = comb[i][1]
            if j < kcal:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-kcal]+rates)

    print(f'#{tc} {dp[N][L]}')