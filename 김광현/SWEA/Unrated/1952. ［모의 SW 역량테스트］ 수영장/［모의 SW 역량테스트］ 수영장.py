T = int(input())
for tc in range(1, T + 1):
    day, month, month_3, year = map(int, input().split())
    swim_days = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = dp[i-1] + (swim_days[i-1]*day)
        dp[i] = min(dp[i], dp[i-1] + month)
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + month_3)
    min_cost = min(dp[12], year)
    print(f'#{tc} {min_cost}')