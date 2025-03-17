N=int(input())
schedule=[list(map(int,input().split())) for _ in range(N)]

dp=[0]*(N+1)

for i in range(N): # 이 날에 상담을 시작한다.
    for j in range(i+schedule[i][0],N+1):
        if dp[j]<dp[i]+schedule[i][1]: # 이날에 상담을 해서 이후에 벌 금액이 큰지
            dp[j]=dp[i]+schedule[i][1] # 이날 이전에 상담을 해서 벌 금액이 큰지 비교
print(dp[N])