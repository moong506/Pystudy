n = int(input())

# 충분히 큰 값(설탕을 정확히 나눌 수 없는 경우를 대비)
INF = 5001
dp = [INF] * (n + 1)  # 0부터 n까지 최소 봉지 개수를 저장할 DP 배열
dp[0] = 0  # 0kg을 만들기 위한 봉지 개수는 0

for i in range(3, n + 1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + 1)  # 3kg 봉지를 사용할 경우
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)  # 5kg 봉지를 사용할 경우

# 만약 dp[n]이 초기 설정값(5001)이면 정확히 만들 수 없는 경우
print(dp[n] if dp[n] != INF else -1)