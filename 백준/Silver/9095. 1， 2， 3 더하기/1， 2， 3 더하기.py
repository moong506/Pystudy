T = int(input())
dp = [0]*11     # 수가 작기 때문에 미리 배열 만듬

# 초기값 설정
dp[0] = 1
dp[1] = 1
dp[2] = 2
# dp 채우기
for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])