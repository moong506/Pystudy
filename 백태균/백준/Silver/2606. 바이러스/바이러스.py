def dfs(S):
    infection = 1
    visited[S] = infection

    for x in adj_list[S]:
        if visited[x] == 0:
            visited[x] = infection
            dfs(x)


N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

dfs(1)

cnt = -1  # 1번 컴퓨터는 제외
for i in range(1, N+1):
    if visited[i] == 1:
        cnt += 1

print(cnt)