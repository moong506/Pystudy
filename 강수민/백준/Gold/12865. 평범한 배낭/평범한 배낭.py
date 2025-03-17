N, K = map(int, input().split())
bag = [[0, 0]]
dp = [[0]*(K+1) for _ in range(N+1)]
# print(dp)

for _ in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(f'{dp[N][K]}')